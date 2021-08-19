(n, s) = map(int, input().split())
alist = [int(x) for x in input().split()]
alist.sort()
if sum(alist[:n - 1]) <= s:
    print('YES')
else:
    print('NO')
