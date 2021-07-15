t, s, x = list(map(int, input().split()))
x -= t
print(["NO", "YES"][(x >= s and x % s in [0, 1])or x == 0])

