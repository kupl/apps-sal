N = int(input())
A_ls = list(map(int, input().split(' ')))
B_ls = list(map(int, input().split(' ')))
rst = 0
for i, val in enumerate(B_ls):
    if A_ls[i] + A_ls[i + 1] >= val:
        rst += val
        if A_ls[i] >= val:
            A_ls[i] -= val
        else:
            A_ls[i + 1] -= val - A_ls[i]
    else:
        rst += A_ls[i] + A_ls[i + 1]
        A_ls[i], A_ls[i + 1] = 0, 0
print(rst)
