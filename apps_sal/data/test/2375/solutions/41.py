# 01:25
a, b = map(int, input().split())
if abs(a - b) <= 1:
    print('Brown')
else:
    print('Alice')
