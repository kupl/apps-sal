n=int(input())
li = []
while not n in li:
  li.append(n)
  if n % 2 == 0:
    n //= 2
  else:
    n = n * 3 + 1
  
print(len(li)+1)
