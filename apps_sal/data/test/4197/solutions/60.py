N = int(input())
rst = [ [] for i in range(N) ]
A_ls = list(map(int, input().split(' ')))
for i, j in enumerate(A_ls):
    rst[j - 1] = i + 1
[ print(i, end=" ") for i in rst ]
