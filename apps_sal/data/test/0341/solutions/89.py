from collections import deque
N,K = map(int,input().split())
R,S,P = map(int,input().split())
Tlist = input()
Answer = 0
def po(x):
    if x == 's':
        return R
    elif x == 'r':
        return P
    else:
        return S
for i in range(K):
    TK = list(Tlist[i::K]).copy()
    TK.append('')
    T2 = TK[0]
    sig = 2
    for i in range(1,len(TK)):
        T1 = T2
        T2 = TK[i]
        if T1 == T2 and i != len(TK)-1:
            sig += 1
        else:
            Answer += po(T1)*(sig//2)
            sig = 2
print(Answer)
