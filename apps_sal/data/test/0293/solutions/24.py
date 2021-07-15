import itertools
import math

x = int(input())
kmax = math.floor((3*x) ** (1/3))
ans = []
for i in range(1, kmax+1):
    if 6*x % (i*(i+1)) == 0:
        s = 6*x // (i*(i+1)) + i - 1
        if s % 3 == 0:
            ans.append((i,s//3))


res = 2*len(ans) - 1 if ans[-1][0] == ans[-1][1] else 2*len(ans)
print(res)
for pair in ans[:-1]:
    print(pair[0], pair[1])

if res%2 == 0: print(ans[-1][0], ans[-1][1])

for pair in reversed(ans):
    print(pair[1], pair[0])

