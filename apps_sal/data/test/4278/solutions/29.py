import collections
N = int(input())
S_ls = []
(cnt, rst) = (0, 0)
for i in range(N):
    S = list(input())
    S.sort()
    val = ''
    S_ls.append(''.join(S))
rst_ls = collections.Counter(S_ls)
for i in rst_ls.values():
    rst += i * (i - 1) // 2
print(rst)
