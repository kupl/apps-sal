import math
for _ in range(int(input())):
    n = int(input())
    s = input()
    r = 0
    for i in range(1, n):
        if s[i - 1] != s[i]:
            continue
        else:
            r += 1
    print(math.ceil(r / 2))
