a = list(map(int, input().split()))
n = a[0]
a = sorted(a[1:])
x = 1234**500000
for i in range(n):
    print('{} '.format(a[i]), end='')
print('')

