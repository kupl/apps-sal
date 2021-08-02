n, t = [int(i) for i in input().split()]
a = [int(j) for j in input().split()]
for i in range(n):
    c = 86400 - a[i]
    t -= c
    if t <= 0:
        print(i + 1)
        break
