
import sys
# sys.stdin=open("data.txt")
input = sys.stdin.readline

n = int(input())

l = list([int(x) - 1 for x in input().split()])

use = []
valid = 1
for i in range(n):
    t = i
    for j in range(n + 5):
        t = l[t]
        if t == i:
            if (j + 1) % 2 == 0: use.append((j + 1) // 2)
            else: use.append(j + 1)
            break
    else:
        valid = 0

if not valid: print("-1")
else:
    # get lcm
    ans = 1
    for i in use:
        t = ans
        while ans % i:
            ans += t
    print(ans)
