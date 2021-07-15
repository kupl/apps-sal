n = int(input())
a = list(map(int, input().split()))

d = {}

for ai in a:
  d[ai] = d.get(ai - 1, 0) + 1

maxRange = 0
endVal = 0
for key in d.keys():
  if (d[key] > maxRange):
    maxRange = d[key]
    endVal = key

startVal = endVal - maxRange + 1
print(maxRange)
for i, val in enumerate(a):
  if (val == startVal):
    print(i+1, end= ' ')
    startVal += 1

