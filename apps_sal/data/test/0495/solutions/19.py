a, k = list(map(int, input().split()))
a = str(a)
l = list(a)
s = ''
while k > 0 and len(l) != 0:
    u = max(l[0:k + 1])
    s += str(u)
    c = l.index(u)
    l.remove(u)
    k -= c
for i in l:
    s += str(i)
print(s)
