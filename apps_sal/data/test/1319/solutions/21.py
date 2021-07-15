m = int(input())
primes = list(map(int, input().split()))
dict = {}
result = 1

for p in primes:
    dict[p] = dict.get(p, 0) + 1

mult = 1
for x in dict.values():
    mult *= x + 1
    mult %= 2*(10**9+6)

for x, y in dict.items():
    result *= pow(x, (y*mult)//2, 10**9 + 7)
    result %= 10**9 + 7

print(result)
