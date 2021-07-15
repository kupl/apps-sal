N = int(input()) 
s = list(map(int,input().split()))
temp=1000000
count=0
for i in range(N):
    if temp>s[i]:
        count =count+1
        temp=s[i]

print(count)

