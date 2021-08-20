(a, b) = map(int, input().split())
if a ** 2 * b % 2 != 0 or a * b ** 2 % 2 != 0:
    print('Yes')
elif a ** 2 * b % 2 == 0 or a * b ** 2 % 2 == 0:
    print('No')
