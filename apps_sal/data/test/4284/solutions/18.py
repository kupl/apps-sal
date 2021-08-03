a = int(input())
for i in range(a):
    z, x, n, m = list(map(int, input().split()))
    if(x * m >= z):
        print(-1)
    else:
        print(min((z - m * x - 1) // (n - m), x))
