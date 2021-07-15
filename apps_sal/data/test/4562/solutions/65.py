N = int(input())

for i in range(int(N**0.5)+3):
  if i**2 > N:
    print((i-1)**2)
    break
