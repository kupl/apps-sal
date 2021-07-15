from math import pi, sin

for i in range(int(input())):
    n = int(input())
    a = 0
    ans = 0
    x = pi - pi * (n - 1) / n
    for j in range(n - 1):
        a += x
        ans += sin(a)
    print(ans)

