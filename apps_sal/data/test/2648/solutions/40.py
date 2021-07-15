N = int(input())
A = sorted(list(map(int,input().split())))
B = set(A)

if len(B)%2==0:
  print(len(B)-1)
else:
  print(len(B))
