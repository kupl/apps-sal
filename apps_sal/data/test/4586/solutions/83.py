n = input()
a = []
for i in range(len(n)):
    a.append(n[i])
if (a[0] == a[1]) & (a[1] == a[2]) or (a[3] == a[2] and a[2] == a[1]):
    print('Yes')
else:
    print('No')
