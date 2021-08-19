from sys import stdin
n = int(stdin.readline())
a = [-1] * n
b = [-1] * n
opened = [0] * n
for i in range(n):
    (a_, b_) = [int(v) for v in stdin.readline().split()]
    a[i] = a_
    b[i] = b_
o1 = [-1] * 1001
o2 = [-1] * 1001
for i in range(n):
    if o1[b[i]] != -1:
        o2[b[i]] = i
    else:
        o1[b[i]] = i
sol = 0
for i in range(n):
    if o1[a[i]] == -1 or (o1[a[i]] == i and o2[a[i]] == -1):
        sol += 1
print(sol)
