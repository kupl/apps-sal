n = int(input())
A = list(map(int, input().split()))

K = 0
while all(a%2 == 0 for a in A):
  A = [a/2 for a in A]
  K += 1
  
print(K)

