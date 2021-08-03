n = int(input())

count = dict()
for i in range(1, 8):
    count[i] = 0
solutions = []

for i in map(int, input().split()):
    count[i] += 1

for i in range(n // 3):
    if count[1] > 0:
        if count[2] > 0:
            if count[4] > 0:
                count[1] -= 1
                count[2] -= 1
                count[4] -= 1
                solutions.append([1, 2, 4])
            elif count[6] > 0:
                count[1] -= 1
                count[2] -= 1
                count[6] -= 1
                solutions.append([1, 2, 6])
        elif count[3] > 0:
            if count[6] > 0:
                count[1] -= 1
                count[2] -= 1
                count[6] -= 1
                solutions.append([1, 3, 6])

if len(solutions) == n // 3:
    for a, b, c in solutions:
        print("{} {} {}".format(a, b, c))
else:
    print(-1)
