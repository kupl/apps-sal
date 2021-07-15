k,a,b = list(map(int, input().split()))
A = []
B = []
sa , sb = 0,0
r = {
    (1,1):(0,0),
    (1,2):(0,1),
    (1,3):(1,0),
    (2,1):(1,0),
    (2,2):(0,0),
    (2,3):(0,1),
    (3,1):(0,1),
    (3,2):(1,0),
    (3,3):(0,0),
}

p = {}

for _ in range(3):
    A.append(list(map(int, input().split())))
for _ in range(3):
    B.append(list(map(int, input().split())))
i = 0
while (i<k):

    if (a,b) in p:
        j, psa, psb = p[(a,b)]
        l = i-j
        psa = sa-psa
        psb = sb-psb
        rep = (k-i)//l
        sa += psa*rep
        sb += psb*rep
        i+=l*rep
        break;
    else:
        p[(a,b)] = (i,sa,sb)

    t = r[(a,b)]
    sa+=t[0]
    sb+=t[1]
    a,b = A[a-1][b-1], B[a-1][b-1]
    i+=1

while (i<k):

    t = r[(a,b)]
    sa+=t[0]
    sb+=t[1]
    a,b = A[a-1][b-1], B[a-1][b-1]
    i+=1

print(sa,sb)



