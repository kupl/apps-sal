n = int(input())
a = 1
b = 1
x = ['o' for _ in range(n)]
while b <= n:
    x[b - 1] = 'O'
    a ^= b
    b ^= a
    a ^= b
    b = a + b
print(''.join(x))
