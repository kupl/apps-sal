N = int(input())
H_ls = list(map(int, input().split(' '))) + [float('inf')]
tmp, val, rst = 0, 0, 0
for i in H_ls:
    if tmp < i:
        rst = max(rst, val)
        val = 0
        tmp = i
    else:
        val += 1
        tmp = i
print(rst)
