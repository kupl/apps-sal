import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

A, B = mapint()
print(100, 100)

white_grid = [['.']*100 for _ in range(50)]
black_grid = [['#']*100 for _ in range(50)]

w, b = A-1, B-1
for i in range(0, 50, 2):
    for j in range(0, 100, 2):
        if b:
            white_grid[i][j] = '#'
            b -= 1
        else:
            break
    else:
        continue
    break

for i in range(1, 50, 2):
    for j in range(0, 100, 2):
        if w:
            black_grid[i][j] = '.'
            w -= 1
        else:
            break
    else:
        continue
    break

for w in white_grid:
    print(''.join(w))
for b in black_grid:
    print(''.join(b))
