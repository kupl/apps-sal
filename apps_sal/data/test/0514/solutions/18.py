import math
t = int(input())
for _ in range(t):
    (n, d) = map(int, input().split())
    tf = True
    for x in range(n + 1):
        if x + math.ceil(d / (x + 1)) <= n:
            print('YES')
            tf = False
            break
    if tf:
        print('NO')
