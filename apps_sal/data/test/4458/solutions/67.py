N = int(input())
P_ls = list(map(int, input().split(' ')))
min_val = 10 ** 6
rst = 0
for i in P_ls:
    if i <= min_val:
        rst += 1
        min_val = i
print(rst)
