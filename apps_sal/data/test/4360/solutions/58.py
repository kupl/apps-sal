a = int(input())
b = list(map(int,input().split()))
A = 1
B = 0
for i in range(a):
  A *= b[i]
for i in range(a):
  B += A/b[i]
print(A/B)
