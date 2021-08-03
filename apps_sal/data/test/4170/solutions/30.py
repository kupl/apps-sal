N = int(input())
H_ls = list(map(int, input().split(' ')))
tmp, val, rst = 0, 0, 0
for i in H_ls:
    if tmp >= i:
        val += 1
        rst = max(rst, val)
        tmp = i
    else:
        rst = max(rst, val)
        val = 0
        tmp = i
print(rst)
