n = int(input())
t = 0
*l, = map(int, input().split())
a = l[:]
s = sorted(range(n), key=lambda x: l[x])
for i in s:
    if l[i] > t:
        t = l[i]
        a[i] = (str(t))
    else:
        t += 1
        a[i] = (str(t))
print(' '.join(a))
