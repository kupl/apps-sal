X = int(input())

while True:
    check = True
    for i in range(2, int(X**0.5) + 1):
        if X % i == 0:
            X += 1
            check = False
            break
    if check:
        print(X)
        break
