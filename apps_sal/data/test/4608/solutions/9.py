#!/usr/local/bin/python3
# https://atcoder.jp/contests/abc065/tasks/abc065_b

N = int(input())
a = [int(input())-1 for _ in range(N)]
ans = 0
cur = 0

visit = [-1] * N
while True:
    # print(cur, visit)
    cur = a[cur]
    ans += 1
    if visit[cur] == -1:
        visit[cur] = ans
    else:
        print(-1)
        return
    if cur == 1:
        print(ans)
        return
