n=int(input())
pi=list(map(int,input().split()))
ci=list(map(int,input().split()))
com=1
for i in range(1,n):
      if ci[i]!=ci[pi[i-1]-1]:
            com+=1
print(com)
