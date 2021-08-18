from bisect import bisect_right

N, M = map(int, input().split())
S = [-i for i, s in enumerate(input()) if s == '0']
S = S[:: -1]

ans = []
now = 0
while S[now] != 0:
    to = bisect_right(S, S[now] + M) - 1

    if to == now:
        print('-1')
        return
    ans.append(S[to] - S[now])
    now = to

ans = ans[:: -1]
print(*ans)
