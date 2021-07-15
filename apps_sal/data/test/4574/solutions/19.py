from collections import Counter
n=int(input())
c=Counter(list(map(int, input().split())))
l=list()
for k,v in c.items():
    for _ in range(v//2):
        l.append(k)

l.sort()
l.reverse()
if len(l)>=2:
    print(l[0]*l[1])
else:
    print(0)
