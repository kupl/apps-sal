N = int(input())
A = list(map(int, input().split()))
ans = 'APPROVED'
for i in range(N):
    if A[i] % 2 != 0:
        continue
    elif A[i] % 6 != 0 and A[i] % 10 != 0:
        ans = 'DENIED'
        break
print(ans)
