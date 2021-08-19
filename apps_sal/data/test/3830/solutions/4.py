import math
T = int(input())
for t in range(T):
    n = int(input())
    a = input()
    d = False
    if a.count('>') == 0:
        print(n)
        continue
    if a.count('<') == 0:
        print(n)
        continue
    ans = 0
    for i in range(n):
        if a[i] == '-' or a[i - 1] == '-':
            ans += 1
    print(ans)
