v1, v2 = list(map(int, input().split()))
t, d = list(map(int, input().split()))

dst = v1

for i in range(2, t + 1):
    for x in range(d):
        if abs(v1 + 1 - v2) <= d * (t - i):
            v1 += 1
        elif abs(v1 - v2) > d * (t - i):
            if v1 > v2:
                v1 -= 1
            else:
                v1 += 1
    dst += v1

print(dst)

