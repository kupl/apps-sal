m, k = list(map(int, input().split()))
n = m
twos = 0
fives = 0
while(n % 2 == 0) or (n % 5 == 0):
    if n % 2 == 0:
        twos += 1
        n //= 2
    if n % 5 == 0:
        fives += 1
        n //= 5
final = n * 2 ** max(k, twos) * 5 ** max(k, fives)
print(final)
