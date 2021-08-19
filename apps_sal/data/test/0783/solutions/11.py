n = int(input())
mas = list(map(int, input().split(' ')))
submas = [0] * n
ma = 0
for i in range(n - 1, -1, -1):
    submas[i] = str(max(ma - mas[i] + 1, 0))
    if ma < mas[i]:
        ma = mas[i]
print(' '.join(submas))
