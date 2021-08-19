import collections
n = int(input())
a = input().split()
a = [int(i) for i in a]
d = collections.Counter(a)
c = 0
b = [0] * 30
b[0] = 2
for i in range(1, 30):
    b[i] = b[i - 1] * 2
for i in a:
    (f, m) = (0, 0)
    for j in b:
        if j - i in d:
            f = 1
            m = j - i
    if f == 1:
        if i == m:
            if d[i] <= 1:
                c += 1
    if f == 0:
        c += 1
    'if i not in d:\n        d[i]=1\n    else:\n        d[i]+=1'
print(c)
