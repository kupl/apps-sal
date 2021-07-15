n, t = map(int, input().split())
times = list(map(int, input().split())) + [0]
for i in range(1, n):
    times[i] += times[i - 1]
l = 0
r = n + 1
while l + 1 < r:
    label = False
    m = (r + l) // 2
    for i in range(m - 1, n):
        if times[i] - times[i - m] <= t:
            label = True
            break
    if label:
        l = m
    else:
        r = m
print(l)
