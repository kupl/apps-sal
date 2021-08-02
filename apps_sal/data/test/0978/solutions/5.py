k = int(input())
z = []
x1 = input()
for i in range(0, len(x1)):
    if (x1[i] != '.'):
        z.append(int(x1[i]))
    else:
        continue

x2 = input()
for l in range(0, len(x2)):
    if (x2[l] != '.'):
        z.append(int(x2[l]))
    else:
        continue


x3 = input()
for y in range(0, len(x3)):
    if (x3[y] != '.'):
        z.append(int(x3[y]))
    else:
        continue

x4 = input()
for s in range(0, len(x4)):
    if (x4[s] != '.'):
        z.append(int(x4[s]))
    else:
        continue


key = len(set(z))

copy = list(set(z))
count = 0
for j in range(0, len(copy)):
    if (z.count(copy[j]) <= 2 * k):
        count += 1
    else:
        count = count


if (count == key):
    print("YES")
else:
    print("NO")
