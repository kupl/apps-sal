(n, a, b, c, t) = map(int, input().split())
tt = [t - int(i) for i in input().split()]
ans = 0
if b >= c:
    print(a * n)
else:
    print(sum(tt) * (c - b) + a * n)
