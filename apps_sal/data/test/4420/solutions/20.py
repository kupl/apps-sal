a = int(input())
for i in range(a):
    x, y, n = list(map(int, input().split()))
    r = (n // x) * x
    if(r + y <= n):
        print(r + y)
    else:
        print(max(r - x + y, y))
