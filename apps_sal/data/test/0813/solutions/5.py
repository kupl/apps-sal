n = int(input().split()[0])
A = [int(s) - 1 for s in input().split()]
for i in range(n):
    print('1' if i in A else '2', end=' ' if i != n - 1 else '')
print('\n')
