from collections import defaultdict
import math
t = input()
s = input()
tomake = defaultdict(lambda: 0)
for i in t:
    if(i == '5'):
        tomake['2'] += 1
    elif(i == '9'):
        tomake['6'] += 1
    else:
        tomake[i] += 1
fro = defaultdict(lambda: 0)
for i in s:
    if(i == '5'):
        fro['2'] += 1
    elif(i == '9'):
        fro['6'] += 1
    else:
        fro[i] += 1
ans = math.inf
for i in list(tomake.keys()):
    ans = min(ans, fro[i] // tomake[i])
print(ans)
