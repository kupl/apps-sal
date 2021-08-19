(x, y) = list(map(int, input().split()))
s = [y, y, y]
k = 0
while sum(s) != x * 3:
    mi = min(s)
    ma = max(s)
    sr = sum(s) - ma - mi
    a = sum([sr, ma]) - 1
    if a > x:
        a = x
    s[s.index(mi)] = a
    k += 1
print(k)
