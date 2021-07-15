x, y = list(map(int, input().split()))
if -1 <= x - y <= 1:
    print('Brown')
else:
    print('Alice')

# abs(x - y) <= 1 → abs(x - y) >= 2
# abs(x - y) >= 2 → abs(x - y) <= 1

