N = int(input())
List = list(map(int,input().split()))
A = sorted(List)

p,q=A[N//2-1:N//2+1]

for i in List:
  print(p if i>=q else q)
