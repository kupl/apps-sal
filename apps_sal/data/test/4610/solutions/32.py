(n, k) = map(int, input().split())
A = list(map(int, input().split()))
L = [0] * n
ans = 0
for a in A:
    L[a - 1] += 1
L = sorted(L)
for i in range(n - k):
    ans += L[i]
print(ans)
