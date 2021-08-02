import itertools as itt
import math

k = int(input())

ans = 0
for i in itt.combinations_with_replacement(range(1, k + 1), 3):
    if i[0] == i[1] and i[0] != i[2]:
        ans += 3 * math.gcd(math.gcd(i[0], i[1]), i[2])
    elif i[1] == i[2] and i[1] != i[0]:
        ans += 3 * math.gcd(math.gcd(i[0], i[1]), i[2])
    elif i[0] == i[1] and i[0] == i[2]:
        ans += math.gcd(math.gcd(i[0], i[1]), i[2])
    else:
        ans += 6 * math.gcd(math.gcd(i[0], i[1]), i[2])

print(ans)
