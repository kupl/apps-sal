(x, y) = list(map(int, input().split()))
n = int(input())
z = y - x
if n == 1:
    print(x % 1000000007)
elif n == 2:
    print(y % 1000000007)
elif n == 3:
    print(z % 1000000007)
else:
    mod = n % 3
    if mod == 0:
        if n // 3 % 2 == 0:
            print(-1 * z % 1000000007)
        else:
            print(z % 1000000007)
    elif mod == 1:
        if n // 3 % 2 == 1:
            print(-1 * x % 1000000007)
        else:
            print(x % 1000000007)
    elif n // 3 % 2 == 1:
        print(-1 * y % 1000000007)
    else:
        print(y % 1000000007)
