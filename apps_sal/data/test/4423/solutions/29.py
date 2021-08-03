N = int(input())
SP = [[input().split(), i + 1] for i in range(N)]
SP_sort = sorted(SP, key=lambda x: (x[0][0], -int(x[0][1])))

for i in range(N):
    print((SP_sort[i][1]))
