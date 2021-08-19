t = int(input())
for i in range(t):
    n = int(input())
    print('7' * (n % 2) + '1' * (n // 2 - n % 2))
