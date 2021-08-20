import math
t = int(input())
for _ in range(t):
    suc = False
    x = int(input())
    for n in range(int(x ** 0.5) + 1, int((4 * x / 3) ** 0.5) + 2):
        if int((n ** 2 - x) ** 0.5) ** 2 == n ** 2 - x:
            mm = int((n ** 2 - x) ** 0.5)
            m = math.floor(n / mm)
            if n ** 2 - (n // m) ** 2 == x:
                print(n, m)
                suc = True
                break
    if not suc:
        print(-1)
