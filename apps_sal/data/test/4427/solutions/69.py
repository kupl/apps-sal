r, D, x_2000 = map(int, input().split())

x = [x_2000] * 11

for i in range(10):
  x[i+1] = r * x[i] - D
  
print(*x[1:], sep='\n')
