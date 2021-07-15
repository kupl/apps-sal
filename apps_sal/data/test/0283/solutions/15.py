def prime(x):
    for i in range(2, 1001):
        if x % i == 0 and i != x:
            return False
    return True


n = int(input())
for m in range(1, 1001):
    if not prime(n * m + 1):
        print(m)
        return

