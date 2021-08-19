(height, n) = list(map(int, input().split()))
s = height
reverted = False
for h in range(height - 1, -1, -1):
    if n > 2 ** h:
        more = True
        n -= 2 ** h
    else:
        more = False
    if more ^ reverted:
        s += 2 * 2 ** h - 1
    reverted = not more
print(s)
