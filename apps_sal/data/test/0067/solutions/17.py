(x, y, z) = list(map(int, input().split()))
num = x - y
if num > 0:
    print('+' if num - z > 0 else '?')
elif num < 0:
    print('-' if num + z < 0 else '?')
elif num == 0:
    print('0' if z == 0 else '?')
