(n, m) = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
c = m
for i in range(n):
    s = (m + b[i] - a[0]) % m
    for j in range(n):
        if (a[j] + s) % m != b[(i + j) % n]:
            break
    else:
        c = min(c, s)
print(c)
