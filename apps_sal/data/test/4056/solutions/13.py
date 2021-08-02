import math
# helpful:
# r,g,b=map(int,input().split())
#list1 = input().split()
# for i in range(len(list1)):
#    list1[i] = int(list1[i])
# print(list1)
# arr = [[0 for x in range(columns)] for y in range(rows)]

n = int(input())
list1 = input().split()
for i in range(len(list1)):
    list1[i] = int(list1[i])
gcd1 = list1[0]
for i in range(n):
    gcd1 = math.gcd(gcd1, list1[i])

val = 0

if(int(math.sqrt(gcd1))**2 == gcd1):
    val -= 1

for i in range(1, int(math.sqrt(gcd1)) + 1):
    if(gcd1 % i == 0):
        val += 2

print(val)
