n = int(input())
n_init = n
m = 0
while n > 0:
    m += n % 10
    n //= 10
print('Yes' if n_init % m == 0 else 'No')
