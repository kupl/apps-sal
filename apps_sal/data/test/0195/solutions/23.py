a, b, c, n = [int(i) for i in input().split()]
k = n - a - b + c
if k < 1 or c > min(a, b) or c > n:
    print(-1)
else:
    print(k)

