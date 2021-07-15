n = int(input())
c=[0]*200
for i in range(n):
    a=list(map(int, input().split()))
    for i in range(1, len(a)):
        c[a[i]]+=1
for i in range(len(c)):
    if c[i]==n:
        print(i, end=' ')
