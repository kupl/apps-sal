(a, b) = list(map(str, input().split(' ')))
ans = False
for i in range(1000):
    if int(a + b) == i ** 2:
        ans = True
print('Yes' if ans else 'No')
