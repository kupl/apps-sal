def prime(x):
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True


n = int(input())
if prime(n):
    print(1)
elif n % 2 == 0 or prime(n - 2):
    print(2)
else:
    print(3)
