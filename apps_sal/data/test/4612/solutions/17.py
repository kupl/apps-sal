lst = input().split()
a = int(lst[0])
b = int(lst[1])

v1 = (a + b) / 2
v2 = (a + b) // 2

if v1 == v2:
    print(v2)
else:
    print(v2 + 1)
