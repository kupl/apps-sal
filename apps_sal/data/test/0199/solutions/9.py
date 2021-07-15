n, s = list(map(int, input().split()))
v = list(map(int, input().split()))
sm = sum(v)
sm -= s
if sm < 0:
    print(-1)
else:
    mn = min(v)
    r = min(mn, sm // n)
    print(r)

