N = int(input())

X = 2*(N//11)

if (N % 11) > 6:
  X += 2
elif (N % 11) > 0:
  X += 1
  
print(X)
