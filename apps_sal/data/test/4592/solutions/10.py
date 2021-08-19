from collections import defaultdict
N = int(input())
prime_counts = defaultdict(int)
for i in range(2, N + 1):
    n = i
    for p in prime_counts:
        while True:
            if n % p == 0:
                prime_counts[p] += 1
                n = n // p
            else:
                break
    if n > 1:
        prime_counts[n] += 1
d = 1
for c in prime_counts.values():
    d *= 1 + c
print(d % (10 ** 9 + 7))
