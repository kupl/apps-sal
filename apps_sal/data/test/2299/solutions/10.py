import sys
(N, M) = list(map(int, input().split()))
G = [list(map(int, input().split())) for i in range(N)]
rmaxv = [0 for i in range(N)]
for i in range(M):
    reach = [0 for j in range(N)]
    for j in range(N - 1, -1, -1):
        if j + 1 == N or not G[j][i] <= G[j + 1][i]:
            reach[j] = 1
        else:
            reach[j] = reach[j + 1] + 1
        rmaxv[j] = max(rmaxv[j], reach[j])
Q = int(input())
ans = []
for qi in range(Q):
    (L, R) = list(map(int, input().split()))
    if rmaxv[L - 1] >= R - L + 1:
        ans.append('Yes\n')
    else:
        ans.append('No\n')
sys.stdout.write(''.join(ans))
