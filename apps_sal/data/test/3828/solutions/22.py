n=int(input())
l=[n]*(n+1)
for c in map(int,input().split()):l[c]=l[c-1]-1
print(min(l))

