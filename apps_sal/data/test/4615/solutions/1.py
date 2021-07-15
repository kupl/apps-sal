A,B,C,D,E,F = map(int,input().split())

concentration = 0
ans = [A*100,0]

water = []
for a in range(F//(A*100) + 1):
  for b in range(((F-a*A*100)//(B*100))+1):
    water.append((a*A+b*B)*100)
    
water = sorted(list(set(water)))

sugar = []
for c in range(F//C + 1):
  for d in range(((F - c*C)//D)+1):
    sugar.append(c*C+d*D)
sugar = sorted(list(set(sugar)))


for wa in water:
  for su in sugar:
    if wa + su <= F:
      if su <= (wa/100)*E:
        if wa != 0:
          if concentration < su/(su+wa):
            concentration = su/(su+wa)
            ans = [su+wa,su]

print(" ".join(map(str,ans)))
