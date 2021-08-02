n, m = list(map(int, input().split()))
l = list(map(int, input().split()))
if n > m:
    print(0)
else:
    r = 1
    for i in range(n):
        for s in range(i + 1, n):
            r = r * abs(l[i] - l[s])
            r = r % m
    print(r)
