N = int(input())
K = int(input())

value = 1

for i in range(N):
  if(value * 2 <= value + K):
    value = value * 2
  else:
    value = value + K

print(value)
