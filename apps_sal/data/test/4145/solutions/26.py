def is_prime(x):
    k = 2
    while k * k <= x:
        if x % k == 0:
            return False
        k += 1
    return True


x = int(input())
while True:
    if is_prime(x):
        print(x)
        break
    else:
        x += 1
