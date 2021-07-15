def rotate(p) :
    return [-p[1]+p[2]+p[3], -p[2]+p[3]+p[0],p[2],p[3]]
def isS(P) :
    X = [P[0][0]*4,P[1][0]*4,P[2][0]*4,P[3][0]*4]
    Y = [P[0][1]*4,P[1][1]*4,P[2][1]*4,P[3][1]*4]
    p = sum(X)//4
    q = sum(Y)//4
    r = [(X[i]-p)**2 + (Y[i]-q)**2 for i in range(4)]
    if len(set(r)) != 1 :
        return False
    for i in range(4) :
        for j in range(i+1,4) :
            if X[i] == X[j] and Y[i] == Y[j] :
                return False

    for i in range(4) :
        for j in range(i+1,4) :
            k,l = list(set([0,1,2,3])-set([i,j]))
            t1 = (X[i] - X[k])**2 + (Y[i]-Y[k])**2
            t2 = (X[i] - X[l])**2 + (Y[i]-Y[l])**2
            t3 = (X[j] - X[k])**2 + (Y[j]-Y[k])**2
            t4 = (X[j] - X[l])**2 + (Y[j]-Y[l])**2
            if t1 == t2 == t3 == t4 : return True
    return False

N = int(input())
for i in range(N) :
    res = []
    P = []
    for j in range(4) :
        p = list(map(int,input().split(' ')))
        P.append(p)
    
    for k1 in range(4) :
        for k2 in range(4) :
            for k3 in range(4) :
                for k4 in range(4) :
                    if isS(P) : res.append(k1+k2+k3+k4)
                    P[3] = rotate(P[3])
                P[2] = rotate(P[2])
            P[1] = rotate(P[1])
        P[0] = rotate(P[0])
    res = min(res) if res else -1
    print(res)
