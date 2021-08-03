import math
for _ in range(int(input())):
    a, k = list(map(int, input().split()))
    for i in range(k - 1):
        d = list(str(a))
        l = int(min(d)) * int(max(d))
        if l == 0:
            break
        a += l
    print(a)
