N = int(input())
fac = [i+2 for i in range(N-1)]
num = 1

for i in range(N-1):
  num = num * fac[i]
  
  fac = [x//fac[i] if x%fac[i] == 0 else x for x in fac]
  #print(fac)

print((num+1))

