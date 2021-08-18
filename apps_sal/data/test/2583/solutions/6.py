def is_prime(n):
    if n == 1:
        return False
    if n == 2 or n == 3 or n == 5:
        return True

    lim = int(n**0.5)
    for d in range(2, lim + 1):
        if n % d == 0:
            return False
    return True


def winnable(n):
    if n == 2:
        return True
    elif not (n - 1) & n:
        return False
    elif n & 1:
        return True
    elif n % 4 == 0:
        return True
    elif is_prime(n >> 1):
        return False
    else:
        return True


for t in range(int(input())):
    n = int(input())
    print("Ashishgup" if winnable(n) else "FastestFinger")
