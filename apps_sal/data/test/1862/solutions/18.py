n = int(input())
l = list(map(int,input().split()))
t = []
for i in range(100001):
    t.append(0)
w = 0
F = 0
for i in l:
    t[i] += 1
    if t[i]==1:
        F += 1
    if w<F:
        w = F
    if t[i]==2:
        F -= 1
    if w<F:
        w = F
print(w)

