def is_not_less_than(ls, ind, key):
    if ls[ind] >= key:
        return True
    else:
        return False
def return_min_ind_whose_value_not_less_than(ls,key):
    r = len(ls)
    l = -1
    while True:
        next_ind = (r+l) // 2
        if is_not_less_than(ls, next_ind, key):
            r = next_ind
        else:
            l = next_ind
        if r - l == 1:
            return r
n_shrine,n_temple,Q = list(map(int,input().split()))
shrine_ls = [0] * (n_shrine+1)
temple_ls = [0] * (n_temple+1)
Q_ls = [0] * Q
for i in range(n_shrine):
    shrine_ls[i] = int(input())
shrine_ls[-1] = float('inf')
for i in range(n_temple):
    temple_ls[i] = int(input())
temple_ls[-1] = float('inf')
for i in range(Q):
    Q_ls[i] = int(input())

for q in Q_ls:
    i_Rshrine = return_min_ind_whose_value_not_less_than(shrine_ls,q)
    Rshrine = shrine_ls[i_Rshrine]
    i_Lshrine = i_Rshrine-1
    Lshrine = shrine_ls[i_Lshrine]

    i_Rtemple = return_min_ind_whose_value_not_less_than(temple_ls,q)
    Rtemple = temple_ls[i_Rtemple]
    i_Ltemple = i_Rtemple-1
    Ltemple = temple_ls[i_Ltemple]
    # Temple,Shrine共に右
    RR = max(Rtemple,Rshrine) - q
    # Temple,Shrine共に左
    if i_Lshrine >= 0 and i_Ltemple >= 0:
        LL = abs(min(Ltemple,Lshrine)-q)
    else:
        LL = float('inf')
    #右templeと左shrine
    if i_Lshrine >= 0:
        RtLs = 2*min(Rtemple-q,q-Lshrine) + max(Rtemple-q,q-Lshrine)
    else:
        RtLs = float('inf')
    # 左templeと右shrine
    if i_Ltemple >= 0:
        LtRs = 2*min(Rshrine-q,q-Ltemple) + max(Rshrine-q,q-Ltemple)
    else:
        LtRs = float('inf')

    print((min(LL,RR,RtLs,LtRs)))


