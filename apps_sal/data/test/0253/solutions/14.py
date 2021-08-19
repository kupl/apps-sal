data = input().split(' ')
k = [int(data[0]), int(data[1]), int(data[2])]
k.sort()
[k1, k2, k3] = k
has_solution = False
if k1 == 1:
    has_solution = True
elif k1 == 2 and k2 == 2:
    has_solution = True
elif k1 == 2 and k2 == 4 and (k3 == 4):
    has_solution = True
elif k1 == 3 and k2 == 3 and (k3 == 3):
    has_solution = True
if has_solution:
    print('YES')
else:
    print('NO')
