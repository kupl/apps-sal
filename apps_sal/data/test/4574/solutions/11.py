import sys
from collections import Counter
n = int(input())
a = list(map(int,input().split()))
box,box2,ans = [],[],0
acnt = dict(Counter(a))
acnt = sorted(acnt.items(), key=lambda x:x[0],reverse=True)
a_val = [acnt[x][1] for x in range(len(acnt))]
a_key = [acnt[y][0] for y in range(len(acnt))]
for i in range(len(a_val)):
	if a_val[i] >= 4:
		box2.append(a_key[i]**2)
	if 2 <= a_val[i]:
		box.append(a_key[i])
box.sort(reverse=True)
if len(box2) >= 2:	
	ans = max(box2)
if len(box) >= 2:
    print(max(ans,(box[0]*box[1])))
    return
print(0)
