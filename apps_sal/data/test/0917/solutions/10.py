n, h, m = map(int, input().split())

A = [h] * n

for i in range(m):
    l, r, mh = map(int, input().split())
    for i in range(l - 1, r):
        A[i] = min(A[i], mh)

ans = 0

for i in A:
    ans += i**2

print(ans)
