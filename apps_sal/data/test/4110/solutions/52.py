from itertools import product

ans = 10**9

D, G = list(map(int, input().split()))
problem = [list(map(int, list(input().split()))) for i in range(D)]

for p in product([True, False], repeat=D):

    point = 0
    num = 0

    for i in range(D):
        if p[i]:
            point += (i + 1) * 100 * problem[i][0] + problem[i][1]
            num += problem[i][0]

    if point >= G:
        ans = min(ans, num)

    for i in reversed(list(range(D))):
        if p[i] == False:
            if point >= G:
                ans = min(ans, num)
                break
            for j in range(problem[i][0]):
                point += (i + 1) * 100
                num += 1
                if point >= G:
                    break
    if point >= G:
        ans = min(ans, num)
print(ans)
