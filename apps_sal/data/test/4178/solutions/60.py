N = int(input())
H_ls = list(map(int, input().split(' ')))
H_ls.reverse()
tmp = float('inf')
for (i, val) in enumerate(H_ls):
    if tmp < val:
        H_ls[i] -= 1
        val -= 1
    tmp = val
if H_ls == sorted(H_ls, reverse=True):
    print('Yes')
else:
    print('No')
