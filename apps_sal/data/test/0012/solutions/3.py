n = int(input())
t = input()
L = [-1]
s = 0
for i in range(n):
    if t[i] == 'S':
        L.append(i)
        s += 1
L.append(n)
m = L[1] - L[0] - 1
for i in range(len(L) - 2):
    if L[i + 2] - L[i] - 1 > m:
        m = L[i + 2] - L[i] - 1
print(min(m, n - s))
