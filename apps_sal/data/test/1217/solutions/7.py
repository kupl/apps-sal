(n, m) = list(map(int, input().split(' ')))
a = list(sorted(map(int, input().split(' '))))
b = list(map(int, input().split(' ')))
c = sorted(set(b))
l = {}
j = 0
for i in c:
    while j < n and a[j] <= i:
        j += 1
    l[i] = j
s = []
for i in b:
    s.append(l[i])
print(' '.join(map(str, s)))
