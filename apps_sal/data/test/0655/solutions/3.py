n = int(input())
(x, y) = list(map(int, input().split()))
if max(x - 1, y - 1) > max(n - x, n - y):
    print('Black')
else:
    print('White')
