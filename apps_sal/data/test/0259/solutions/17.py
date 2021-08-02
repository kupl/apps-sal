n, t = map(int, input().split())
l = []
for i in range(n):
    s, d = map(int, input().split())
    if s < t:
        if (t - s) % d == 0:
            q = (t - s) // d
        else:
            q = (t - s) // d + 1
        l.append([s + q * d, i + 1])
    else:
        l.append([s, i + 1])
l.sort(key=lambda x: x[0])
print(l[0][1])
