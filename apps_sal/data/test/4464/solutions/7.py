import sys
A, B, C = list(map(int, input().split()))

for i in range(100):
  if C == (A*i%B):
    print("YES")
    return
print("NO")

