from sys import stdin
from math import *

line = stdin.readline().rstrip().split()
n = int(line[0])

numbers = list(map(int, stdin.readline().rstrip().split()))
numbers2 = list(map(int, stdin.readline().rstrip().split()))

growRateAccum = 0
topAccum = 0
bottomAccum = 0

accumsB = [0]*n
accumsT = [0]*n

growRateAccum = 0
accum = 0
for i in range(n-1, -1, -1):
    accum += numbers[i] * (((n-i)*2)-1-1)
    growRateAccum += numbers[i]
    if i<n-1:
        growRateAccum += numbers2[i + 1]
    accum += growRateAccum
    accumsB[i] = accum

growRateAccum = 0
accum = 0
for i in range(n-1, -1, -1):
    accum += numbers2[i] * (((n-i)*2)-1-1)
    growRateAccum += numbers2[i]
    if i<n-1:
        growRateAccum += numbers[i + 1]
    accum += growRateAccum
    accumsT[i] = accum


#for i in range(n-1, -1, -1):
#    if i % 2 == 0:
#        if i == n-1:
#            accums[i] = numbers2[i]
#        else:
 #           bottomAccum += numbers2[i]*((n-i)*2-1)
  #          growRateAccum += numbers2[i] + numbers[i+1]
   #         bottomAccum += growRateAccum
#        accums[i] = bottomAccum
 #   if i % 2 == 1:
  #      if i == n-1:
  #          accums[i] = numbers2[i]
  #      else:
   #         topAccum += numbers[i]*((n-i)*2-1)
   #         growRateAccum += numbers[i] + numbers2[i+1]
   #         topAccum += growRateAccum
   #         accums[i] = topAccum
cMax = 0
currAccum = 0

growRateAccum = sum(numbers[1::]) + sum(numbers2[1::])

for i in range(n):
    if i%2==0:
        #estoy en top:
        cMax = max(cMax, currAccum+accumsT[i])
    else:
        cMax = max(cMax, currAccum + accumsB[i])
    if(i<n-1):
        if i%2 == 0:
            currAccum += numbers2[i] + growRateAccum * 2
        else:
            currAccum += numbers[i] + growRateAccum * 2
        growRateAccum -= numbers[i+1]
        growRateAccum -= numbers2[i+1]
print(cMax)


