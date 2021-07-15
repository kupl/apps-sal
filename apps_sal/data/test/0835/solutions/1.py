
def bin (a, b, c, n, m, k, pn, pm, pk, r):
    [L, R] = [0, (r + n + m + k) * 100]
    while R - L > 1:
        M = (R + L) // 2
        a2 = max(M * a - n, 0)
        b2 = max(M * b - m, 0)
        c2 = max(M * c - k, 0)
        if a2 * pn + b2 * pm + c2 * pk <= r:
            L = M
        else:
            R = M
    return L

str = input()
[a, b, c] = [0, 0, 0]
[n, m, k] = [int(i) for i in input().split()]
for i in str:
    if i == 'B':
        a += 1
    elif i == 'S':
        b += 1
    else:
        c += 1
[pn, pm, pk] = [int(i) for i in input().split()]
r = int(input())
print(bin(a, b, c, n, m, k, pn, pm, pk, r))

