n, k = map(int, input().split())
for i in range(k):
    if n % 5 == 0:
        n //= 5
    if n % 2 == 0:
        n //= 2
print(n * 10 ** k)
