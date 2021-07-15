K, N = map(int, input().split(' '))
A_ls = list(map(int, input().split(' ')))
rst = -1
for i in range(N):
    l = A_ls[(i + 1) % N] - A_ls[i]
    if l < 0:
        l = K - A_ls[i] + A_ls[(i + 1) % N]
    if rst == -1:
        rst = l
    else:
        rst = max(rst, l)
print(K - rst)
