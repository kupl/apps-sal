n = int(input())
(x, y) = list(map(int, input().split()))
if abs(x - 1) + abs(y - 1) <= abs(x - n) + abs(y - n):
    print('White')
else:
    print('Black')
