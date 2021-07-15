H,W = map(int,input().split())
c = [list(map(int,input().split())) for i in range(10)]
A = [list(map(int,input().split())) for i in range(H)]
ma = [1001]*10
ma[1] = 0
use = [i for i in range(10)]
use.remove(1)
from itertools import permutations
for i in range(1,10):
    l = list(permutations(use,i))
    for j in l:
        cost =0
        first = pre = j[0]
        border = ma[first]
        k = 1
        while cost < border and k < i:
            cost += c[pre][j[k]]
            pre = j[k]
            k += 1
        cost += c[pre][1]
        ma[first] = min(border,cost)
ans = 0
for i in A:
    for j in i:
        if j != -1:
            ans += ma[j]
print(ans)
