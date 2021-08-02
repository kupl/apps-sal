n = int(input())

y = input().split()
x = [int(f) for f in y]
z = x[:]
zeros = []
while (z.count(0) > 0):
    z.remove(0)
    zeros.append(0)


count = 0
count1 = 0
q = list(set(z))
for i in range(0, len(q)):
    key = q[i]
    if (z.count(key) == 2):
        count += 1
    if (z.count(key) == 1):
        count = count
    if (z.count(key) > 2):
        count1 = count1 - 1
        break

if (count1 == 0):
    print(count)
else:
    print(-1)
