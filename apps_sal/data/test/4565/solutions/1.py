N = int(input())
S = list(input())

e_count = 0
for s in S:
  if s == 'E':
    e_count += 1

min_inv = float('infinity')
    
for s in S:
  if s == 'E':
    e_count -= 1
  
  min_inv = min(e_count, min_inv)
  
  if s == 'W':
    e_count += 1

print(min_inv)

