T = int(input())
for t in range(T):
    n = int(input())
    s1 = list(input())
    s2 = list(input())

    ct = 0
    idx = []
    for i in range(n):
        if s1[i] != s2[i]:
            ct += 1
            idx.append(i)

    
    if ct == 2:
        s1[idx[0]], s2[idx[1]] = s2[idx[1]], s1[idx[0]]
        if s1 == s2:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

