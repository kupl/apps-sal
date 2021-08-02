N = int(input())
T = list(map(int, input().split()))
M = int(input())
px = [list(map(int, input().split())) for i in range(M)]

sumTime = sum(T)

for i in range(M):
    print(sumTime - T[px[i][0] - 1] + px[i][1])
