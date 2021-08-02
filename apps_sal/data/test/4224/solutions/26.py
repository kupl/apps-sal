import numpy as np
n = int(input())
a = np.array(list(map(int, input().split())))

ans = 0
for x in a:
    while x % 2 == 0:
        ans += 1
        x //= 2

print(ans)
