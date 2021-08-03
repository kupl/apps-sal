n = int(input())
lst = []

for i in range(n):
    x = int(input())
    lst.append(x)

a = max(lst)
b = []
for i in range(n):
    if (lst[i] == a):
        b.append(i)

if (len(b) > 1):
    for i in range(n):
        print(a)

else:
    lst[b[0]] = 0
    c = max(lst)
    for i in range(n):
        if (i == b[0]):
            print(c)
        else:
            print(a)
