n = int(input())

a, b = map(int, input().split())

if (a - 1) + (b - 1) <= (n - a) + (n - b):
    print('White')
else:
    print('Black')
