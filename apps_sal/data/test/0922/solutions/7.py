(n, a) = [int(i) for i in input().split()]
t = [int(i) for i in input().split()]
s = 0
for i in t:
    s += i
k = []
for i in range(n):
    k.append(0)
    if s - a < t[i]:
        k[i] += t[i] - s + a - 1
    if t[i] - (a - n + 1) > 0:
        k[i] += t[i] - (a - n + 1)
print(*k)
