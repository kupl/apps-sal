def cnt(n):
    a = [0] * 10
    c = 0
    b = 0
    while n != 0:
        a[n % 10] += 1
        if a[n % 10] == 1:
            c += 1
        n //= 10
        b += 1
    if b == c:
        return True
    else:
        return False


n = int(input().strip())
i = 1
while not cnt(n + i):
    i += 1
print(n + i)
