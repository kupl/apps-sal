from collections import *
n = int(input())
v = list(map(int,input().split()))
if len(set(v))==1:
    print(len(v)//2)
    return
n_even = v[0::2]
n_odd = v[1::2]
a = Counter(n_even).most_common()+[(0,0)]
b = Counter(n_odd).most_common()+[(0,0)]
#print(a)
#print(b)
if a[0][0] == b[0][0]:
    ans = min(n-a[0][1]-b[1][1],n-a[1][1]-b[0][1])
else:
    ans = n - a[0][1] - b[0][1]
print(ans)
