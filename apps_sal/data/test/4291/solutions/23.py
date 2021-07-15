N,Q = map(int,input().split())
S = input()
lr = [list(map(int,input().split()))for _ in range(Q)]
l = [lr[i][0] for i in range(Q)]
r = [lr[i][1] for i in range(Q)]
#print(lr)
#print(l)
#print(r)

c = [0] * N
cnt = 0

for i in range(N-1):
    if S[i:i+2] == 'AC':
        c[i+1]=c[i]+1
    else:
        c[i+1]=c[i]
    #c[i] = S[:i].count('AC')

#print(c)

for i,j in zip(l,r):
    #print(sum(c[:j])-sum(c[:i]))
    #l,r = map(int,input().split())
    print(c[j-1]-c[i-1])
