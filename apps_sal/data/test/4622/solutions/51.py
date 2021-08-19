N = int(input())
A = list(map(int, input().split()))
A.sort()
ans = 'YES'
for i in range(1, N):
    if A[i - 1] == A[i]:
        ans = 'NO'
        break
print(ans)
