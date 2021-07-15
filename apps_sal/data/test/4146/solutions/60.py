n = int(input())
v = list(map(int,input().split()))

v1 = [v[i] for i in range(n) if i%2 == 1]
v2 = [v[i] for i in range(n) if i%2 == 0]
            
import collections

v1n = collections.Counter(v1)
v2n = collections.Counter(v2)

v1ns = v1n.most_common(2)
v2ns = v2n.most_common(2)

a = v2ns[0][1]
c = v1ns[0][1]
if v1ns[0][0]!=v2ns[0][0]:
    print(n-a-c)
else:
    if len(v1ns)==1:
        d = 0
    else:
        d = v1ns[1][1]
    if len(v2ns)==1:
        b = 0
    else:
        b = v2ns[1][1]
    print(min(n-a-d,n-c-b))
