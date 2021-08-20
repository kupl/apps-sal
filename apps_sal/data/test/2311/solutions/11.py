def get_dividers(k):
    dividers = set()
    for i in range(1, int(k ** 0.5) + 2):
        if k % i == 0:
            dividers.add(i)
            dividers.add(k // i)
    return sorted(list(dividers))


(n, m, k) = map(int, input().split())
dividers = get_dividers(k)
A = list(map(int, input().split()))
B = list(map(int, input().split()))


def count(A, d):
    in_a_row = 0
    res = 0
    for a in A:
        if a == 1:
            in_a_row += 1
            if in_a_row >= d:
                res += 1
        else:
            in_a_row = 0
    return res


a_d = {}
b_d = {}
for d in dividers:
    a_d[d] = count(A, d)
    b_d[d] = count(B, d)
res = 0
for d in dividers:
    res += a_d[d] * b_d[k // d]
print(res)
