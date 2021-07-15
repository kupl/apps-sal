n = int(input())
a = []
for i in range(n):
    a.append(input())
b = []
for i in range(n):
    b.append(input())
c = n
for i in a:
    if i in b:
        c -= 1
        b.remove(i)
print(c)

