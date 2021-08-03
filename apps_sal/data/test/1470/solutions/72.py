x = int(input())
cnt = 0
v = [0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2]
print(2 * (x // 11) + v[x % 11])
