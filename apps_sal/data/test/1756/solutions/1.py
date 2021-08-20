def sumprog(a, b):
    return (a + b) * (b - a + 1) // 2


(n, x) = map(int, input().split())
d = list(map(int, input().split())) * 2
max_hugs = 0
i = 0
j = 0
days = 0
hugs = 0
while i < n:
    if days + d[j] <= x:
        days += d[j]
        hugs += sumprog(1, d[j])
        j += 1
    else:
        max_hugs = max(max_hugs, hugs + sumprog(d[j] - (x - days) + 1, d[j]))
        hugs -= sumprog(1, d[i])
        days -= d[i]
        i += 1
print(max_hugs)
