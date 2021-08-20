a = []
b = []
for i in range(int(input())):
    a.append(int(input()))
b = list(set(a))
if len(b) != 2:
    print('NO')
elif a.count(b[0]) == a.count(b[1]):
    print('YES')
    b.sort()
    print(*b)
else:
    print('NO')
