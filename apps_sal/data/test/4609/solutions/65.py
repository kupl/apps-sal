N = int(input())
A = [int(input()) for i in range(N)]
A.sort()

ans = 0
cnt = 1
for i in range(1, N):
    if A[i] == A[i-1]:
        cnt += 1
    else:
        if cnt % 2 != 0:
            ans += 1
        cnt = 1
if cnt % 2 != 0:
    ans += 1
print(ans)
