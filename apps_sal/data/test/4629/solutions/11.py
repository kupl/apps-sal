def isgood(n):
    while n > 0:
        if n % 3 > 1:
            return False
        n //= 3
    return True


q = int(input())
for _ in range(q):
    n = int(input())
    while not isgood(n):
        n += 1
    print(n)
