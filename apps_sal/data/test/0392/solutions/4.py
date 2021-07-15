def factorize(n):
    result = { }
    i = 2
    while i * i <= n:
        d, m = divmod(n, i)
        if m == 0:
            count = 0
            while m == 0:
                count += 1
                n = d
                d, m = divmod(n, i)
            result[i] = count
        i += 1
    result[n] = 1
    return result

n = int(input())
result = 1
for k, v in list(factorize(n).items()):
    result *= k
print(result)

