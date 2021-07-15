N = int(input())
K = int(input())

ans = 1

def A(n):
   return 2 * n

def B(n):
   return n + K

for i in range(N):
   if A(ans) <= B(ans):
      ans = A(ans)
   else:
      ans = B(ans)

print(ans)
