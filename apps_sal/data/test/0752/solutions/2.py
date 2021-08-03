n = int(input())

a = []
b = []

for i in range(n):
    a.append(input())

for i in range(n):
    b.append(input())
counter = 0
for i in range(n):
    if (a[i] not in b):
        counter += 1
    else:
        b.remove(a[i])

print(counter)
