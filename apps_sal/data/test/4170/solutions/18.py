N = int(input())
H_ls = list(map(int, input().split(' '))) + [float('inf')]
(rst, tmp, val) = (0, 0, 0)
for i in H_ls:
    if i > tmp:
        rst = max(rst, val)
        val = 0
    else:
        val += 1
    tmp = i
print(rst)
