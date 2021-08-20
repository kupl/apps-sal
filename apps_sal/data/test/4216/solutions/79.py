import math
n = int(input())
a = 0
for i in range(1, int(math.sqrt(n)) + 1):
    if n % i == 0:
        a = i
b = n // a
j = 0
while True:
    m = b / 10 ** j
    if m >= 1 and m < 10:
        ans = j + 1
        break
    j += 1
print(ans)
