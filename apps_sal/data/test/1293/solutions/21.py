N = int(input())
B = [ int(b) for b in input().split() ]
level = 0
step = 0
for i in range(N):
  if not B[i] == level:
    step += abs(B[i]-level)
    level = B[i]
print(step)
