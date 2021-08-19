import bisect
import numpy
H = int(input())
ans = 1
HP = 2
tmp = 1
while True:
    if H < HP:
        break
    else:
        tmp *= 2
        ans += tmp
        HP *= 2
print(ans)
