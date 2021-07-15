n, mind, v = int(input()), [0] * 3, [0] * 3
for i in range(3):
    mind[i], v[i] = map(int, input().split())
t = sum(v)
for i in range(2, -1, -1):
    c = max(0, min(t - n, v[i] - mind[i]))
    v[i] -= c
    t -= c
print(v[0], v[1], v[2])
