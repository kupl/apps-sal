N = int(input())
while True:
    check = True
    for i in range(2, int(N ** 0.5) + 1):
        if N % i == 0:
            N += 1
            check = False
            break
    if check:
        print(N)
        break
