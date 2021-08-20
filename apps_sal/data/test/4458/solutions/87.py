N = int(input())
P_ls = list(map(int, input().split(' ')))
(rst, min_val) = (0, 10 ** 6)
for i in P_ls:
    if min_val >= i:
        rst += 1
        min_val = i
print(rst)
