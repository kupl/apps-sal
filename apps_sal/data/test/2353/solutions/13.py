import math
for nt in range(int(input())):
    (a, b, c, d) = map(int, input().split())
    if b >= a:
        print(b)
        continue
    if d >= c:
        print(-1)
        continue
    diff = c - d
    t = c
    left = a - b
    print(b + math.ceil(left / diff) * c)
