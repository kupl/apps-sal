N = int(input())
T = list(map(int, input().split()))
M = int(input())
for i in range(1, M + 1):
    tmp = list(map(int, input().split()))
    tmp2 = T[tmp[0] - 1]
    T[tmp[0] - 1] = tmp[1]
    print(sum(T))
    T[tmp[0] - 1] = tmp2
