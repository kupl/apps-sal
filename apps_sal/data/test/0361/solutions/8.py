l = list(input())
l1 = list('CODEFORCES')
c = 0
d = 0
for i in range(min(len(l),len(l1))):
    if l[i] == l1[i]:
        c += 1
    else:
        break

l = l[::-1]; l1 = l1[::-1]
for i in range(min(len(l),len(l1))):
    if l[i] == l1[i]:
        d += 1
    else:
        break
if c+d >= len(l1):
    print('YES')
else:
    print("NO")

