from itertools import combinations
def out1(a,b,c):
    if a<0 or b<0 or c<0:
        return 0
    if a==1 and b==0 and c==0:
        return 1
    return a*(out2(a-1,b,c)+out3(a-1,b,c))
def out2(a,b,c):
    if a<0 or b<0 or c<0:
        return 0
    if a==0 and b==1 and c==0:
        return 1
    return b*(out1(a,b-1,c)+out3(a,b-1,c))
def out3(a,b,c):
    if a<0 or b<0 or c<0:
        return 0
    if a==0 and b==0 and c==1:
        return 1
    return c*(out2(a,b,c-1)+out1(a,b,c-1))
def column(matrix, i):
    return [row[i] for row in matrix]
    
N, T = [int(x) for x in input().split()]
A = []
s = 0
for i in range(N):
    A.append([int(x) for x in input().split()])
for i in range(1,N+1):
    comb = list(combinations(A, i))
    for x in comb:
        if sum(column(x,0))==T:
            a = column(x,1).count(1)
            b = column(x,1).count(2)
            c = column(x,1).count(3)
            s+=(out1(a,b,c)+out2(a,b,c)+out3(a,b,c))
print(s%1000000007)
