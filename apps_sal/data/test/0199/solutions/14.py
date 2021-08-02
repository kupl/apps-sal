n, s = map(int, input().split())
l = [*map(int, input().split())]
sm = sum(l)
if sm < s:
    print(-1)
    return
m = min(l)
s -= sm - m * n
if s <= 0:
    print(m)
else:
    print(m - (s + n - 1) // n)
