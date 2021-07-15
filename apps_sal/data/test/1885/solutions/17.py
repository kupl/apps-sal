import math
n = int(input())
a = int(math.factorial(n)/(math.factorial(5)*math.factorial(n - 5)))
b = int(math.factorial(n)/(math.factorial(6)*math.factorial(n - 6)))
c = int(math.factorial(n)/(math.factorial(7)*math.factorial(n - 7)))
print(int(a + b + c))

