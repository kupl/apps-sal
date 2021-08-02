N, M = [int(n) for n in input().split()]
dp = [-1] * N
ans = 0
for _ in range(M):
    s, c = [int(n) for n in input().split()]
    if dp[s - 1] == -1:
        dp[s - 1] = c
    elif dp[s - 1] != c:
        ans = -1

if ans == -1 or (dp[0] == 0 and N != 1):
    print(-1)
else:
    ans = ''.join([str(n) if n != -1 else '0' for n in dp])
    if ans[0] == '0' and N > 1:
        print('1' + ans[1:])
    else:
        print(ans)
