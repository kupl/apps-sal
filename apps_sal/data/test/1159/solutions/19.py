from math import sqrt 
n = int(input())
def prost(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

f = n
while not prost(f):
    f += 1
print(f)
for i in range(1, n):
    print(i, i + 1)
print(n, 1)
g = 1
f = f - n
while f:
    print(1 + g - 1, n - g)
    g += 1
    f -= 1

