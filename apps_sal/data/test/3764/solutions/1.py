'''
import random
la=100
a=[[]]
for i in range(0,la):a[0].append(random.randint(1,1001))
x=random.randint(1,1001)
print('x: ',x)
a.sort()
print('origin a',a[0])
'''
s = input().split()
n = int(s[0])
k = int(s[1])
x = int(s[2])
a = [[]]
s = input().split()
for i in range(n):
    a[0].append(int(s[i]))

a[0].sort()
for i in range(1, k + 1):
    a.append([a[i - 1][t] ^ (x * ((t + 1) % 2)) for t in range(len(a[i - 1]))])
    a[i].sort()
    for t in range(i):
        if a[i] == a[t]:
            flag = True
            break
    if(t != i - 1):
        break

if(k == 0):
    tag = 0
elif(i == k):
    tag = k
else:
    tag = (k - i + 1) % (t - i) + i - 1
print(max(a[tag]), min(a[tag]))
