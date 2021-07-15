n = int(input())
print((n * n + 1) // 2)
ret = ['C.' * (n // 2) + ('C' if n % 2 == 1 else '')]
ret.append('.C' * (n // 2) + ('.' if n % 2 == 1 else ''))
for i in range(n):
    print(ret[i % 2])

