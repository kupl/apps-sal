(a, b) = input().split()
a = int(a)
b = int(b)
c = 0
for i in range(a, b + 1):
    i = str(i)
    if i[0] == i[4] and i[1] == i[3]:
        c += 1
print(c)
