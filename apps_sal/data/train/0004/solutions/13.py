for j in range(int(input())):
    n = int(input())
    c = list(map(int, input().split()))
    index = [0] * n
    for i in range(n):
        index[c[i] - 1] = i
    ma = 0
    mi = n
    ans = ['0'] * n
    # print(index)
    for k in range(n):
        ma = max(index[k], ma)
        mi = min(index[k], mi)
        # print(k,mr,index[k]-index[0])
        if ma - mi <= k:
            ans[k] = '1'
    print(''.join(ans))
