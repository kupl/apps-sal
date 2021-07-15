N = int(input())

for i in range(1, 10**9):
  if i**2 == N:
    print((i**2))
    break
  elif i**2 > N:
    print(((i-1)**2))
    break

