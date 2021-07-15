#n = int(input())
from collections import defaultdict
god = defaultdict(int)
n, m = [int(i) for i in input().split(" ")]
fuck = [int(i) for i in input().split(" ")]
b = [int(i) for i in input().split(" ")]
for i in fuck:
    god[i] += 1
ans = []
f = dict( zip(fuck, range(1, n+1)) )
s = set( fuck )
answ = "Possible"
for i in b:
    if not i in s:
        answ = "Impossible"
        break
    elif god[i] > 1:
        answ = "Ambiguity"
    else:
        ans.append(f[i])

print(answ)
if answ == "Possible":
    for i in ans:
        print(i, end=' ')

