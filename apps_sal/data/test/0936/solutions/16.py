n = int(input())
l = list(map(int, input().split()))
d1 = dict()
d = dict()
s = set()
s1 = set()
for i in l:
    if i in s:
        d[i] += 1
    else:
        d[i] = 1
    s.add(i)

max1 = 0
for i in d:
    max1 = max(max1, d[i])
for i in l:
    if i in s1:
        d1[i] += 1
    else:
        d1[i] = 1
    s1.add(i)
    if d1[i] == max1:
        print(i)
        break
