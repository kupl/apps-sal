n, k = map(int, input().split())
if n == 1:
    print(0)
else:
    if k >= n // 2:
        print(n*(n-1)//2)
    else:
        s = 0
        for i in range(1, k + 1):
            s += 1 + 2 * (n - 2*i)
        print(s)
