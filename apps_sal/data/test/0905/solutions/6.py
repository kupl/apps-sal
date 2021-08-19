(n, s) = list(map(int, str.split(input())))
r = -1
for _ in range(n):
    (x, y) = list(map(int, str.split(input())))
    if x < s or (x == s and y == 0):
        r = max(r, 100 - (y or 100))
print(r)
