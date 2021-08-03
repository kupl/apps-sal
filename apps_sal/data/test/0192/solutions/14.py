x, y = list(map(int, input().split()))
s = [y, y, y]
k = 0
while sum(s) != x * 3:
    minn = min(s)
    maxx = max(s)
    sr = sum(s) - maxx - minn
    a = sum([sr, maxx]) - 1
    if a > x:
        a = x
    s[s.index(minn)] = a
    k += 1
print(k)
