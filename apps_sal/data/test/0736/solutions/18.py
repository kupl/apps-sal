import math
(n, m) = list(map(int, input().split()))
res = 0
if n == 0:
    print(0)
    quit()
if m > n:
    print(-1)
    quit()
'if n%2==0:\n    res = (n//2)\n\nelse:\n    res = (n//2+1)\nprint(res+n%m)'
for i in range((n + 1) // 2, n + 1):
    if i % m == 0:
        print(i)
        quit()
