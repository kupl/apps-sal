p = int(input())
while True:
    q = int(p**0.5)
    for i in range(2, q + 1):
        if p % i == 0:
            p += 1
            break
    else:
        print(p)
        break
