from math import ceil
p = {i: 0 for i in 'abcdefghijklmnopqrstuvwxyz'}
t = input()
for i in t: p[i] += 1
p = {i: p[i] for i in p if p[i] > 0}
n = int(input())
if len(p) > n: print(-1)
elif len(t) > n:
    r = [[p[i], p[i], 1, i] for i in p]
    for i in range(n - len(p)):
        j = max(r)
        j[2] += 1
        j[0] = j[1] / j[2]
    print(ceil(max(r)[0]))
    print(''.join(j[3] * j[2] for j in r))     
else: print('1\n' + t * (n // len(t)) + t[: n % len(t)])  
