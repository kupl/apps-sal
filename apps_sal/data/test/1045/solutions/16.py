n = int(input())

a = [i for i in range(10000)]
i = 0
res = 0
while n > 0:
    if n < sum(a[:i + 1]):
        break
    res += 1
    n -= sum(a[:i + 1])
    i += 1
print(res - 1)
