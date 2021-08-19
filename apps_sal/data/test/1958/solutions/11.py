(n, p) = map(int, input().split())
data = [input() for i in range(n)]
q = 0
pol = 0
for elem in data[::-1]:
    if elem == 'halfplus':
        pol += 1
        q += 0.5
        q *= 2
    else:
        q *= 2
print(int(q * p - pol * p / 2))
