
a = int(input())
x = list(map(int, input().split(' ')))
y = list(map(int, input().split(' ')))
z = list(map(int, input().split(' ')))

x.sort()
y.sort()
god = False
for i in range(min(len(x), len(y))):
    if x[i] != y[i]:
        print(x[i])
        god = True
        break

if not god:
    print(x[-1])
z.sort()
god = False
for i in range(min(len(z), len(y))):
    if y[i] != z[i]:
        print(y[i])
        god = True
        break

if not god:
    print(y[-1])
