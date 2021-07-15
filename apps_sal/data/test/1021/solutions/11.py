n = int(input())

L = [int(x) for x in input().split()]

S = [int(x) for x in input().split()]

D1 = [0]
D2 = [0]

for i in range(n-1):
    D1.append(L[i+1]-L[i])
    D2.append(S[i+1]-S[i])

D1.sort()
D2.sort()
if (D1 == D2) and (L[0] == S[0]):
    print('Yes')
else:
    print('No')
