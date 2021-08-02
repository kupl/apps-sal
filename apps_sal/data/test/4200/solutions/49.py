N, M = [int(s) for s in input().split()]
ls = [int(s) for s in input().split()]
ls = sorted(ls, reverse=True)
border = sum(ls) / (4 * M)
if ls[M - 1] >= border:
    print('Yes')
else:
    print('No')
