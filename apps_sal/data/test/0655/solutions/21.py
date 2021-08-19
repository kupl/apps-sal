n = int(input())
(x, y) = map(int, input().split())
dw = abs(1 - x) + abs(1 - y)
db = abs(n - x) + abs(n - y)
if db < dw:
    print('Black')
else:
    print('White')
