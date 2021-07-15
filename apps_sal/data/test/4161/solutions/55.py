import math
k = int(input())


total = 0

for x in range(1,k+1):
    for y in range(x,k+1):
        for z in range(y,k+1):
            if x == y == z:
                total += x
            elif x == y or y == z:
                total += 3 * math.gcd(math.gcd(x,y),z)
            else:
                total += 6 * math.gcd(math.gcd(x,y),z)

print(total)

