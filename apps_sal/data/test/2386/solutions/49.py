n = int(input())
A = list(map(int, input().split()))
for i in range(n):
    A[i] -= (i + 1)
A.sort()
ans = 0
b = A[n // 2]
for a in A:
    ans += abs(a - b)
print(ans)
