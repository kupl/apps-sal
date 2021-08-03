import math

s, p = map(int, input().split())
ans = False
for i in range(1, int(math.sqrt(p)) + 1):
    if p % i == 0:
        if s == ((p / i) + i):
            ans = True
            break

if ans:
    print('Yes')
else:
    print('No')
