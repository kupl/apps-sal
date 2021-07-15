x = int(input())
ans = 0
for i in range(x, 10000000):
    is_prime_bool = True
    for j in range(2, i - 1):
        if i % j == 0:
            is_prime_bool = False
            break
    if is_prime_bool:
        print(i)
        break
