a = int(input())
c = []
d = []
while a > 0:
    b = input().split()
    c.append(b[0])
    d.append(b[1])
    a -= 1
e = 0
for i in c:
    for j in d:
        if i == j:
            e += 1
print(e)
