N = int(input())
D, X = map(int, input().split())

for _ in range(N):
  A = int(input())
  X += 1 + (D-1)//A

print(X)
