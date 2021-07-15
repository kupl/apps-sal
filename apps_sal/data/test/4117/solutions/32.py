from itertools import combinations

N=int(input())
L=list(map(int,input().split()))

count=0

for a,b,c in combinations(L,3):
  if a+b>c and a+c>b and b+c>a and a!=b and b!=c and a!=c:
    count+=1
print(count)
