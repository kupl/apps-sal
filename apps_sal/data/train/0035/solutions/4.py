import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    e = list(map(int, input().split()))
    e = sorted(e)
    ans = 0
    cnt = 0
    max_ = 0
    for i in range(n):
        cnt += 1
        max_ = max(e[i], max_)
        if max_ <= cnt:
            ans += 1
            max_ = 0
            cnt = 0
    print(ans)
