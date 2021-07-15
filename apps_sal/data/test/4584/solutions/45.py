n=[0]*int(input())
for i in map(int,input().split()): n[i-1]+=1
print(*n,sep="\n")    
