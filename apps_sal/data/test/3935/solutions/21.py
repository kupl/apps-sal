n = int(input())
u = list(map(int, input().split()))
a = []
for i in range(n):
    a.append(len(bin(u[i] & -u[i])[2:]))
x = [0] * 61
for i in range(len(a)):
    x[a[i]] += 1
mx = max(x)
p = -1
for i in range(61):
    if x[i] == mx:
        p = i
        break
q = []
for i in range(n):
    if a[i] != p:
        q.append(u[i])
print(len(q))
print(' '.join(map(str, q)))
