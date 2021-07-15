
from fractions import gcd
i = int(input())
full = i // 2520
rest = i%2520
ct = 576*full
for asdf in range(1, rest+1):
    if gcd(asdf, 2520) == 1:
        ct += 1
print(ct)

