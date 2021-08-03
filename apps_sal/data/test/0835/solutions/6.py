t = input()
n = list(map(int, input().split()))
p = list(map(int, input().split()))
r = int(input())
q = [t.count('B'), t.count('S')]
q.append(len(t) - q[0] - q[1])
n = [n[i] for i in range(3) if q[i]]
p = [p[i] for i in range(3) if q[i]]
q = [q[i] for i in range(3) if q[i]]
m = len(q)
a = min(n[i] // q[i] for i in range(m))
b = max((n[i] + r // p[i]) // q[i] for i in range(m)) + 1
while b - a > 1:
    c = (a + b) // 2
    if sum(max(0, (c * q[i] - n[i]) * p[i]) for i in range(m)) > r:
        b = c
    else:
        a = c
print(a)
