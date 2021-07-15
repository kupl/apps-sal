n = int(input())

seen = {1, n}
for i in range(1, int(n**0.5) + 2):
    if n % i == 0:
        seen.add(i)
        seen.add(n // i)

print(len(seen))
