n = int(input())
num = list(map(int, input().split()))

tot1 = 0
tot2 = 0

for i in range(n):
    tot1 += (i+1)

for i in range(n-1):
    tot2 += num[i]
miss = tot1 - tot2
print(miss)

