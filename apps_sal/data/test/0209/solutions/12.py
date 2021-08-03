x, y = list(map(int, input().split()))
n = int(input())
result = n % 6
if result == 1:
    print(x % 1000000007)
elif result == 2:
    print(y % 1000000007)
elif result == 3:
    print((y - x) % 1000000007)
elif result == 4:
    print((-x) % 1000000007)
elif result == 5:
    print((-y) % 1000000007)
elif result == 0:
    print((x - y) % 1000000007)
