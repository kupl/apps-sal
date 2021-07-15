n = int(input())
a = list(map(int,input().split()))
cnt = 0
i,j = 0,0
while i<n and j<n:
    if a[i]==j+1:
        cnt+=1
        j+=1
    i+=1
print(-1 if 1 not in a else n - cnt)
