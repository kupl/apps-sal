n = int(input())
inst = input()

dir_ = dict(U=(0,1), D=(0,-1), L=(-1, 0), R=(1, 0))
ct = 0
for i in range(n):
    x, y = (0, 0)
    for j in range(i, n):
        dx, dy = dir_[inst[j]]
        x += dx
        y += dy
        ct += x == 0 and y == 0

print(ct)

