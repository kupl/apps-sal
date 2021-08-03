import math
n = int(input())
s = math.ceil(math.sqrt(n))
h = 10**5
for i in range(1, s + 1):
    if n % i == 0:
        if h > max(len(str(i)), len(str(int(n / i)))):
            h = max(len(str(i)), len(str(int(n / i))))
print(h)
