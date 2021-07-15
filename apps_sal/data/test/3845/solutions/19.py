A,B=map(int,input().split())

U=[['#' for j in range(100)] for i in range(50)]
for w in range(A-1):
    s=w//50;t=w%50
    U[s*2][t*2]='.'

D=[['.' for j in range(100)] for i in range(50)]
for b in range(B-1):
    u=b//50;v=b%50
    D[u*2+1][v*2]='#'

print(100,100)
for Ui in U:
    print(''.join(Ui))
for Di in D:
    print(''.join(Di))
