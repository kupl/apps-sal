N=int(input())
As=sorted(list(map(int,input().split())))
c=0
for i in range(N-1):
    c+=(As[i]==As[i+1])
print('YNEOS'[c>0::2])
