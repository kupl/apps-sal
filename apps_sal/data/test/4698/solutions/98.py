n = int(input())
T = list(map(int, input().split()))
m = int(input())
D = [tuple(map(int, input().split())) for _ in range(m)]

sum_T = sum(T)
for i in range(m):
    print((sum_T - T[D[i][0] - 1] + D[i][1]))
