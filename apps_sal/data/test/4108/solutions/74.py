def solve():
    S = input()
    n = len(S)
    S1 = [1]
    k = 1
    for i in range(1, n):
        if S[i] not in S[:i]:
            k += 1
            S1.append(k)
        else:
            num = S1[S.find(S[i])]
            S1.append(num)
    return S1


S1 = solve()
T1 = solve()
if S1 == T1:
    print('Yes')
else:
    print('No')
