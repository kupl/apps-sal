(n, m) = list(map(int, input().split()))
flags = [False for i in range(n * 4 + 1)]
for i in range(1, len(flags)):
    if i <= m:
        flags[i] = True
mass = []
for i in range(1, n * 2, 2):
    if flags[i + n * 2]:
        mass.append(i + n * 2)
    if flags[i]:
        mass.append(i)
    if flags[i + n * 2 + 1]:
        mass.append(i + n * 2 + 1)
    if flags[i + 1]:
        mass.append(i + 1)
print(' '.join(map(str, mass)))
