a, b, c = map(int, input().split())
hist = []

ans = 'NO'
for i in range(1, b+1):
  mod = (a*i) % b
  if mod == c:
    ans = 'YES'
    break
  elif mod in hist:
    break
  hist.append(mod)
    
print(ans)
