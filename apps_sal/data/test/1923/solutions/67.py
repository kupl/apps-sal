N = int(input())
A = list(map(int, input().split()))
A.sort()
ans = 0
for i in range(0, len(A), 2):
    ans += min(A[i], A[i + 1])
print(ans)
