a = input().split()
n = int(a[0])
x = int(a[1])
y = int(a[2])
a = input()
groups = 0
add = True
for i in range(n):
    if add == True and a[i] == '0':
        groups += 1
        add = False
    if a[i] == '1':
        add = True
tot1 = groups * y
tot2 = (groups - 1) * x + y
if abs(tot1) > abs(tot2):
    print(tot2)
else:
    print(tot1)
