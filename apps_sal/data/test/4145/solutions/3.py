def prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


X = int(input())
while True:
    if prime(X):
        break
    else:
        X += 1
print(X)
