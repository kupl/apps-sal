(x, y) = map(int, input().split())
msg = 'No'
for a in range(1, x + 1):
    if 2 * a + 4 * (x - a) == y or 4 * a + 2 * (x - a) == y:
        msg = 'Yes'
print(msg)
