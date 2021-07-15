inputs = list(map(int, str(input()).split(" ")))
t, s, x = inputs
dx = x - t

print((dx == 0 or (dx >= s and (dx % s in [0, 1]))) and "YES" or "NO")

