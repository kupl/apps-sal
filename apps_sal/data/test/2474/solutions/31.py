n = int(input())
c = sorted(list(map(int, input().split())))
p = 10 ** 9 + 7

print(((sum([(n + 2 - i) * ci for i, ci in enumerate(c, 1)]) * pow(4, n - 1, p)) % p))

