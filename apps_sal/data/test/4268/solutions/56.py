import numpy as np
import math
n, d = map(int,input().split())
x_l = [ np.array(list(map(int, input().split()))) for _ in range(n)  ]

ans = 0
p = set()
for i,x in enumerate(x_l):
    for j,y in enumerate(x_l):
        if i != j:
            if str(min([i,j]))+'_'+str(max([i,j])) not in p:
                d = math.sqrt(sum((x-y)**2))
                if d.is_integer():
                    ans += 1
                    p.add(str(min([i,j]))+'_'+str(max([i,j])))
print(ans)
