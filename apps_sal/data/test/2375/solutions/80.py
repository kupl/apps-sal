a, b = list(map(int, input().split()))
cnt = 1
if abs(a - b) <= 1:
    print('Brown')
else:
    print('Alice')
