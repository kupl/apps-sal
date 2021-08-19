v = []
for i in range(int(input())):
    v.append(1)
    while len(v) >= 2 and v[-1] == v[-2]:
        v.pop()
        v[-1] += 1
print(' '.join(map(str, v)))
