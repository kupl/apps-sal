N, M = list(map(int, input().split()))
keep = [[] for i in range(N)]
keep2 = []


for i in range(M):
    p, y = list(map(int, input().split()))
    keep[p - 1].append([i, p, y])


for i in range(N):
    keep[i] = sorted(keep[i], key=lambda x: x[2])

for i in range(N):
    biggest = len(keep[i])
    j = 0
    while j < biggest:
        keep[i][j][2] = j + 1
        j += 1
    keep2 += keep[i]

keep2 = sorted(keep2, key=lambda x: x[0])

for i in range(M):
    ans = ''
    ans += '0' * (6 - len(str(keep2[i][1]))) + str(keep2[i][1])
    ans += '0' * (6 - len(str(keep2[i][2]))) + str(keep2[i][2])
    print(ans)

