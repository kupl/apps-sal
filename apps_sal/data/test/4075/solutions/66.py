import math
N, M = list(map(int, input().split()))
switch = [0] * N
pattern = 2 ** N
ans = 0
for i in range(M):
  temp = input().split()[1:]
  for j in temp:
    switch[int(j) - 1] += (1 << i )
  
p = list(map(int, input().split()))
pbin = 0
temp = 1
for i in p:
  pbin += i * temp
  temp *= 2

for i in range(pattern):
  temp = 0
  j = 0
  while i > 0:
    if i & 1 == 1 :
      temp = temp ^ switch[j]
    j += 1
    i = i >> 1
  if pbin == temp:
    ans += 1
print(ans)

