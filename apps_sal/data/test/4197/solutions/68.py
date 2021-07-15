N = int(input())
A_ls = list(map(int, input().split(' ')))
rst = [ [] for i in range(N) ]
for idx, val in enumerate(A_ls):
    rst[val - 1] = idx + 1
[ print(i, end=" ") for i in rst ]
