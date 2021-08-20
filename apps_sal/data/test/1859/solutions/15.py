def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return False
    return True


n = int(input())
c = 0
while True:
    if n % 2 == 0:
        c += n // 2
        break
    if is_prime(n):
        c += 1
        break
    for i in range(2, n):
        if is_prime(i) and n % i == 0:
            break
    n -= i
    c += 1
    if n == 0:
        break
print(c)
