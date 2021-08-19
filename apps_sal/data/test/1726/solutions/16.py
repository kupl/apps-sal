(n, t) = map(int, input().split())
a = list(map(int, input().split()))
k = 0
for i in range(len(a)):
    k += 86400 - a[i]
    if k >= t:
        print(i + 1)
        break
