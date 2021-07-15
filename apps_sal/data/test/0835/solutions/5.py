t = input()
n = list(map(int, input().split()))
p = list(map(int, input().split()))
q = [t.count('B'), t.count('S')]
q.append(len(t) - q[0] - q[1])

n = [n[i] for i in range(3) if q[i]]
p = [p[i] for i in range(3) if q[i]]
q = [q[i] for i in range(3) if q[i]]
m = len(q)

r = int(input())
k = [n[i] // q[i] for i in range(m)]

while r > 0:
    u = min(k)
    v = [j for j in range(m) if k[j] == u]
    for i in v:
        r -= p[i] * (q[i] - n[i] % q[i])
        k[i] += 1
        n[i] = q[i] * k[i]
    if len(v) == m: break
    
if r < 0: print(u)
else:
    u += 1
    if r > 0: u += r // sum(q[i] * p[i] for i in range(m))
    print(u)    
