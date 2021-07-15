n = int(input())
a = list(map(int, input().split()))

x = 100001

p = [-1] * x
l = [-1] * x
t = 0

for i in range(n):
    if p[a[i]] == -1:
        p[a[i]] = 0
        l[a[i]] = i
    elif p[a[i]] == 0:
        p[a[i]] = i - l[a[i]]
        l[a[i]] = i
    elif p[a[i]] > 0:
        if p[a[i]] == i - l[a[i]]:
            l[a[i]] = i
        else:
            p[a[i]] = -2
s=""
for i in range(x):
    if p[i] >= 0:
        t += 1
        s += str(i)+" "+ str(p[i])+"\n"
print(t)
print(s)
