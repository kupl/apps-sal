num = int(input())
for testcase in range(1, num+1):
    [a, b, n, S] = [int(i) for i in input().split()]
    S-=(n*min(a, S//n))
    if(S>b): print('NO')
    else: print('YES')
