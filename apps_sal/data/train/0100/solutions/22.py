import sys
reader = (list(map(int, s.split())) for s in sys.stdin)


def sweets(r, g, b):
    total = g - r
    g -= total
    b -= total
    if b > r + g:
        total += r + g
    else:
        total += (r + b + g) // 2
    return total


(t,) = next(reader)
for _ in range(t):
    (r, g, b) = sorted(list(next(reader)))
    ans = sweets(r, g, b)
    print(ans)
