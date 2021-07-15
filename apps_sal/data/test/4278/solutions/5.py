import collections
N = int(input())
ls, rst = [], 0
for i in range(N):
    s = list(input())
    s.sort()
    ls.append(''.join(s))
rst_ls = collections.Counter(ls)
for i in rst_ls.values():
    rst += (i * (i - 1)) // 2
print(rst)
