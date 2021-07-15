N = int(input())
yakusu = []

for i in range(1,int((N**(0.5))+1)):
  if N % i == 0:
    j = int(N / i)
    yakusu.append([i,j])
    
min_dis = 1000000000000000000000000000000000000000000000000000

for k in range(len(yakusu)):
  distance = yakusu[k][0] - 1 + yakusu[k][1] - 1
  if distance < min_dis:
    min_dis = distance
    
print(min_dis)

