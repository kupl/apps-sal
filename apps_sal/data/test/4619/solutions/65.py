W,H,N = (int(T) for T in input().split())
XYA = [[0],[W],[0],[H]]
for TN in range(0,N):
    X,Y,A = (int(T) for T in input().split())
    if A in [1,2]:
        XYA[A-1].append(X)
    else:
        XYA[A-1].append(Y)
CW = min(XYA[1])-max(XYA[0])
CH = min(XYA[3])-max(XYA[2])
if CW>=0 and CH>=0:
    print(CW*CH)
else:
    print(0)
