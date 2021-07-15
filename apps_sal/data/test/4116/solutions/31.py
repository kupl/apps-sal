N = int(input())  
result="No"
for i in range(10):
  for j in range(10):
    if N==i*j:
      result="Yes"
      break
print(result)
