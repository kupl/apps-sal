from itertools import permutations

N,M = map(int,input().split())
AB = [0 for i in range(M)]

for i in range(M):
  ab = list(map(int,input().split()))
  AB[i] = ab

count = 0
nums = [i for i in range(1,N+1)]
pers =permutations(nums,N)
for i in pers:
  if i[0] == 1:
    flag1 = 0
    for j in range(N-1):
      flag2 = False
      for k in range(M):
        if (i[j] == AB[k][0] and i[j+1] == AB[k][1]) or (i[j] == AB[k][1] and i[j+1] == AB[k][0]):
          flag2 = True
          #print(i,i[j],i[j+1],AB[k])
      if flag2:
        flag1 += 1
    if flag1 == N-1:
      #print(i)
      count += 1
print(count)
