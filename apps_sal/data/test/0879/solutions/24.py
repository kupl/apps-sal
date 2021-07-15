n = int(input())
l = [0]+ list(map(int,input().split()))
c = n-1
k=[n]
while(l[c] != 1):
    k.append(l[c])
    c = l[c]-1
k.append(1)
for i in k[::-1]:
    print(i,end=' ')

