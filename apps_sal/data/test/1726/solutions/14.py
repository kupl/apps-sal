(n, t) = map(int, input().split())
a = list(map(int, input().split()))
i = 0
while t > 0:
    t -= 86400 - a[i]
    i += 1
print(i)
