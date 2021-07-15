N = int(input())
odd = 0
even = 0
for i in range(1, N+1):
  if i % 2 != 0:
    odd += 1
print(odd/N)
