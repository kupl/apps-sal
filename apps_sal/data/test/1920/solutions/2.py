v = [[0] * 367 for i in range(2)]
for i in range(int(input())):
    c = input().split()
    s = int(c[0] == 'M')
    for j in range(int(c[1]), int(c[2]) + 1):
        v[s][j] += 1
print(2 * max((min(x, y) for (x, y) in zip(v[0], v[1]))))
