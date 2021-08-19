N = int(input())
H_ls = list(map(int, input().split(' '))) + [float('inf')]
(rst, val, tmp) = (0, 0, 0)
for i in H_ls:
    if i <= tmp:
        val += 1
        tmp = i
    else:
        rst = max(rst, val)
        val = 0
        tmp = i
print(rst)
