N = int(input())
A1 = list(map(int,input().split()))
A2 = list(map(int,input().split()))

s = []

for i in range(N):
  a = sum(A1[0:i+1])+sum(A2[i:])
  s.append(a)

print(max(s))
