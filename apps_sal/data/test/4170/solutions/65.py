N = int(input())
A = list(map(int, input().split()))
ans = 0
num = 0
for i in range(1, N):
    if A[i - 1] < A[i]:
        ans = max(ans, num)
        num = 0
    else:
        num += 1
ans = max(ans, num)
print(ans)
