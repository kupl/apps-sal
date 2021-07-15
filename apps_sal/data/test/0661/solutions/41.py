import sys
M, K = map(int,input().split())
if M == 0:
    if K == 0:
        print(*[0, 0])
    else:
        print(-1)
    return

if M == 1:
    if K == 0:
        print(*[0, 1, 1, 0])
    else:
        print(-1)
    return

N = 2 ** M

if K >= N:
    print(-1)
    return

ans = []

for i in range(N):
    if i != K:
        ans.append(i)

ans.append(K)

for i in range(N-1,-1,-1):
    if i != K:
        ans.append(i)

ans.append(K)

print(*ans)
