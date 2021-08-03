n, t = list(map(int, input().split()))
a = [86400 - int(x) for x in input().split()]
s = 0
for i in range(n):
    s += a[i]
    if s >= t:
        print(i + 1)
        break
