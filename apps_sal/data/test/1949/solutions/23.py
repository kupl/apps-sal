n, k = [int(x) for x in input().split()]
L = [int(x) for x in input().split()]
L.sort()
D = {}
for i in L:
    if not i in D:
        D[i] = 1

S = list(D.keys())
S.sort()
start = None
for i in range(0,len(S)):
    if S[i] != 0:
        start = i
        break
    
s = 0
for i in range(0,k):
    if start == None or start >= len(S):
        print(0)
    elif S[start] <= s:
        print(0)
    else:
        print(S[start]-s)
        s += S[start]-s
        start +=1

