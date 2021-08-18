n, x, y = list(map(int, input().split()))
s = input().replace('1', ' ')
z = len(s.split())
print(z and (z - 1) * min(x, y) + y)
