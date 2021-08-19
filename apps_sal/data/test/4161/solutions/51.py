import math
K = int(input())
sum = 0
for i in range(1, K + 1):
    for j in range(1, K + 1):
        temp = math.gcd(i, j)
        for k in range(1, K + 1):
            sum += math.gcd(temp, k)
print(sum)
