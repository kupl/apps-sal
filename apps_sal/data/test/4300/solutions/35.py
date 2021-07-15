import itertools
total = 0
recovery = 0
n = int(input())
di = list(map(int, input().split()))
for x in itertools.combinations(di, 2):
  #print(x)
  recovery = x[0] * x[1]
  total += recovery
  #print(total)
print(total)
