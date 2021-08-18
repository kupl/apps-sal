A, B = list(map(int, input().split()))
h, w = 100, 100

Grid = [list('

A -= 1
B -= 1
for i in range(0, 50, 2):
    for j in range(0, 100, 2):
        if A > 0:
            Grid[i][j]='.'
            A -= 1
        else:
            break
    else:
        continue
    break

for i in range(99, 50, -2):
    for j in range(0, 100, 2):
        if B > 0:
            Grid[i][j]= '
            B -= 1
        else:
            break
    else:
        continue
    break

print((100, 100))
for i in range(100):
    print((''.join(Grid[i])))
