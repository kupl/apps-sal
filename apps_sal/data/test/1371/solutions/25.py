import math

s = int(input())
l = s//3
count = 0

for i in range(1,l+1):
    count += math.factorial(s-3*i+i-1)//(math.factorial(i-1)*math.factorial(s-3*i))
    #print(math.factorial(s-3*i+i-1)/(math.factorial(i-1)*math.factorial(s-3*i)))

print(count%(10**9+7))
