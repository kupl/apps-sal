import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
Query = [list(map(int, input().split())) for _ in range(M)]

L = 2**N
seg = [0] * (2 * L - 1)

# initialize
for i in range(L):
    seg[i + L - 1] = A[i]

k = L - 1
c = 0
while k > 0:
    if c % 2 == 0:
        for i in range((k - 1) // 2, k):
            seg[i] = seg[2 * i + 1] | seg[2 * i + 2]
    else:
        for i in range((k - 1) // 2, k):
            seg[i] = seg[2 * i + 1] ^ seg[2 * i + 2]
    c += 1
    k = (k - 1) // 2

# update and return v


def update(k, a):
    k += L - 1
    seg[k] = a
    c = 0
    while k > 0:
        k = (k - 1) // 2
        if c % 2 == 0:
            seg[k] = seg[2 * k + 1] | seg[2 * k + 2]
        else:
            seg[k] = seg[2 * k + 1] ^ seg[2 * k + 2]
        c += 1
    return seg[0]


for p, b in Query:
    ans = update(p - 1, b)
    print(ans)
