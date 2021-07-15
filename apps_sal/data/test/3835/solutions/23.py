x = int(input())
mass = []
for i in range(x):
    l = list(map(int, input().split()))
    mass += [l]
res = [0 for i in range(x)]
res[0] = int(((mass[0][1] * mass[0][2]) // mass[1][2]) ** 0.5)
for i in range(1, x):
    res[i] = int(mass[0][i] // res[0])
print(*res)
