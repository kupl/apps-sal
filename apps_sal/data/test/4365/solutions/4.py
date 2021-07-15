a = int(input())
odd = 0
even = 0
for i in range(1, a+1):
  if i%2 == 1:
    odd += 1
  if i%2 == 0:
    even += 1

print(odd*even)  
