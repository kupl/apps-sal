n = int(input())
a = list(map(int,input().split()))
import collections
b = collections.Counter(a).most_common()
li4 = []
li2 = []
ansli = []
for k in b:
    if k[1]>=4:
        li4 +=[k[0]]
        ansli += [k[0]**2]
    if k[1]>=2:
        li2 +=[k[0]]

if len(li2)>=2:
    li22 = sorted(li2)
    ansli += [li22[-1]*li22[-2]]
if ansli:
    print(max(ansli))
else:
    print(0)
