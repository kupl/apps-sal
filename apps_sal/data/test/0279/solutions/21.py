v1, v2 = [int(c) for c in input().split()]
t, d = [int(c) for c in input().split()]


dist = v1
i = 1

while(i <= t - 2):
    dist += min(v1 + i * d, (v2 + (t - 1) * d) - i * d)
    i += 1

dist += v2
print(dist)
