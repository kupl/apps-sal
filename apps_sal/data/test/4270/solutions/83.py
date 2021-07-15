N = int(input())
ls = list(map(int, input().split(' ')))
ls.sort()
rst = ls[0]
if N >= 2:
    for i in ls[1:]:
        rst = (rst + i) / 2
print(rst)
