a = [[],[]]
for i in range(2):
    a[0].append(int(input()))
for i in range(2):
    a[1].append(int(input()))
a[0].sort()
a[1].sort()
print(a[0][0] + a[1][0])
