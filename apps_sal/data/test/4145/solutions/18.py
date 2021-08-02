def isPrime(num):
    mod = 2
    for i in range(2, num):
        if num % i == 0:
            mod += 1
            break
    if mod == 2:
        return True
    else:
        return False


x = int(input())
while True:
    if isPrime(x):
        print(x)
        break
    else:
        x += 1
