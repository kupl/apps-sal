np = [int(u) for u in input().split()]
n, p = np
s = [tuple(int(u) for u in input().split()) for i in range(n)]


def count_multiples(l, r, p):
    return r // p - (l - 1) // p


def E_X_i(i):
    i %= n
    l_i = s[i][0]
    l_j = s[i + 1][0]
    r_i = s[i][1]
    r_j = s[i + 1][1]
    p_i = count_multiples(l_i, r_i, p) / (1 + r_i - l_i)
    p_j = count_multiples(l_j, r_j, p) / (1 + r_j - l_j)
    pr = p_i * p_j + (1 - p_i) * p_j + (1 - p_j) * p_i
    return pr * 2 * 1000


s.append(s[0])
E_X = sum(E_X_i(i) for i in range(n))
print(E_X)
