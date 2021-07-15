n, m = map(int, input().split())
f, s = 0, 0
p = 0
for i in list(map(int, input().split())):
    p += i
    if p < 0:
        f = min(f, p)
    if p > 0:
        s = max(s, p)
print(0 if s > m or -f > m or m - s < -f else m - s + f + 1)
