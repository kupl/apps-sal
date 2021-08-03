l = int(input())
n = input()

ind = []

for i in range(1, l):
    if n[i] == '0':
        continue
    ind.append((abs(i - (l / 2)), i))

ind.sort()
sol = -1

for i in range(min(4, len(ind))):
    (x, y) = ind[i]
    curr = int(n[:y]) + int(n[y:])
    if sol == -1 or curr < sol:
        sol = curr

print(sol)
