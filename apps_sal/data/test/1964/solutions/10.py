qNumbers = int(input())

k = list(map(int, input().split()))

minScnds = k[0] * 15

itms = list(map(int, input().split()))

for i in range(k[0]):
    minScnds += itms[i] * 5
  
for i in range(1, qNumbers):
    scnds = k[i] * 15
    itms = list(map(int, input().split()))
    for j in range(k[i]):
        scnds += itms[j] * 5
    minScnds = min(scnds, minScnds)

print (minScnds)
