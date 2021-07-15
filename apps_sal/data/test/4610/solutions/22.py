from collections import Counter
a,b=map(int, input().split())
c = Counter(list(map(int, input().split())))
cnt = 0
l = []
m = []

for x,y in c.items():
    l += [y]
    m += [x]

M = len(m)
L = sorted(l)
if M <= b:
    print(0)
if M > b:
    for i in range(M-b):
        cnt += L[i]
    print(cnt)
