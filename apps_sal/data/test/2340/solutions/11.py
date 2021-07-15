import bisect
import sys
input = sys.stdin.readline


q = int(input())
for _ in range(q):
    h, n = map(int, input().split())
    p = list(map(int, input().split())) + [0]
    cnt = 1
    ans = 0
    pos = h
    i = 1
    while True:
        if i >= n+1:
            break
        if pos == p[i] + 1:
            pos = p[i]
            cnt += 1
            i += 1
        else:
            pos = p[i] + 1
            if cnt % 2 == 0:
                ans += 1
                cnt = 1
    print(ans)
