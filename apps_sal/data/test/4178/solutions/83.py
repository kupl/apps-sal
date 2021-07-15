N = int(input())
H_ls = list(map(int, input().split(' ')))
H_ls.reverse()
tmp = float('inf')
for i, val in enumerate(H_ls):
    if val > tmp:
        val -=1
        H_ls[i] = val
    tmp = val
if H_ls == sorted(H_ls, reverse=True):
    print('Yes')
else:
    print('No')
