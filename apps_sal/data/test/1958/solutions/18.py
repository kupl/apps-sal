n, p = map(int, input().split())
a = sum(1 << i for i in range(n) if input() == 'halfplus')
print(sum(a // (1 << i) * p // 2 for i in range(n)))
