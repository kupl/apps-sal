def dp(prev, ind):
    nonlocal dar, n, con, gym
    if ind >= n:
        return 0
    if (prev, ind) not in dar:
        m = dp('free', ind+1)+1
        if prev != 'con' and con[ind]:
            m = min(m, dp('con', ind+1))
        if prev != 'gym' and gym[ind]:
            m = min(m, dp('gym', ind+1))
        dar[(prev, ind)] = m

    return dar[(prev, ind)]
    

dar = {}
n = int(input())
L = [int(x) for x in input().split()]
con = [x&1 for x in L]
gym = [x&2 for x in L]
print(dp('free', 0))


