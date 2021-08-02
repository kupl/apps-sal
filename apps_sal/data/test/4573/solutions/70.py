N = int(input())
X = list(map(int, input().split()))
sort_X = sorted(X)

mid_ls = [sort_X[N // 2 - 1], sort_X[N // 2]]

for i in range(N):
    if X[i] >= mid_ls[1]:
        print(mid_ls[0])
    else:
        print(mid_ls[1])
