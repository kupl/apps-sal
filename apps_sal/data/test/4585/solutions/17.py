import math
X = int(input())
ruto = math.ceil(math.sqrt(2 * X)) + 1
kari = ruto ** 2 + ruto
ans = 1
for i in range(ruto - 1, 0, -1):
    if i ** 2 + i < 2 * X:
        ans = i + 1
        break
    kari = i ** 2 + i
print(ans)
