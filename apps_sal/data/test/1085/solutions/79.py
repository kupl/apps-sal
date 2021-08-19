def div(n):
    r = int(n ** (1 / 2))
    for i in range(1, r + 1):
        if n % i == 0:
            yield i
            if i * i != n:
                yield (n // i)


n = int(input())
count = len(list(div(n - 1))) - 1
for i in div(n):
    if i > 1:
        x = n
        while x % i == 0:
            x //= i
        if x % i == 1:
            count += 1
print(count)
