N = int(input())
D, X = map(int, input().split())
mass = 0

for n in range(N):
  A = int(input())
  i = 0
  day = 1
  while day <= D:
    day = i*A + 1
    i += 1

  mass += (i-1)


result = mass + X
print(result)
