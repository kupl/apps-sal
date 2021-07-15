A, B = map(int, input().split())

k = (A + B) / 2
print(int(k)) if k.is_integer() else print('IMPOSSIBLE')
