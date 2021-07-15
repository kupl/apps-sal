def prime(b):
    i = 1
    if b == 1:
        return 1
    count = 0
    while i * i <= b:
        if b % i == 0:
            if i * i != b:
                count += 2
            else:
                count += 1
        i += 1
    return count
b = int(input())
print(prime(b))

