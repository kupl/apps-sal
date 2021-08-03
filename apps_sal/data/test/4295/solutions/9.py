n, k = map(int, input().split())
if n % k == 0:
    print(0)
else:
    nx = n % k
    if nx < abs(nx - k):
        print(nx)
    else:
        print(abs(nx - k))
