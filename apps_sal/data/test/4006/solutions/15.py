n = int(input())
seen = set()
while n not in seen:
    seen.add(n)
    n += 1
    while n % 10 == 0:
        n //= 10
print(len(seen))
