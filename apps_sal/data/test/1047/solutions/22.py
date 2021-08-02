a = input()
j = 0
b = []
for i in a:
    if j < int(i):
        j = int(i)
print(j)
for i in range(j):
    b.append(0)
mult = 1
for i in a[::-1]:
    for k in range(int(i)):
        b[k] += mult
    mult *= 10
for i in range(j):
    print(b[i], end=' ')
