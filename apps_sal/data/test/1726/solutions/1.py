n, t = map(int, input().split())
a = list(map(int, input().split()))
for i in range(1, n + 1):
    t -= 86400 - a[i - 1]
    if (t <= 0):
        print(i)
        break
