n = int(input())
fx = sum(map(int, list(str(n))))
print(['No', 'Yes'][int(n % fx == 0)])
