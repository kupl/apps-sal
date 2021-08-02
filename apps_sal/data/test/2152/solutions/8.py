import sys

n = int(input())
menor = 10000000
sum = 0
for i in range(n):
    line = input()
    v = [int(x) for x in line.split()]
    if(v[1] < menor):
        menor = v[1]
    sum += menor * v[0]
print(sum)
