import math
s, p = map(int, input().split())
for i in range(1, int(math.sqrt(p)) + 1):
    if p % i == 0 and i + (p // i) == s:
        print("Yes")
        return
else:
    print("No")
