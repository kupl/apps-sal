lst = input().split()
A = int(lst[0])
B = int(lst[1])
C = int(lst[2])
L = []
for i in range(1, B + 1):
    L.append(A * i % B)
if C in L:
    print('YES')
else:
    print('NO')
