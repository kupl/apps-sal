def I():
    return list(map(int, input().split()))


(c, v0, v1, a, l) = I()
rd = 0
day = 0
while rd < c:
    canread = min(v0 + day * a, v1)
    start = max(rd - l, 0)
    rd = start + canread
    day += 1
print(day)
