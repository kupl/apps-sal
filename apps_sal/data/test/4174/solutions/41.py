n, x = map(int, input().split())
l = list(map(int, input().split()))
d = 0
i = 0
while d <= x and i <= n:
    if i == n:
        i += 1
    else:
        d += l[i]
        i += 1
print(i)
