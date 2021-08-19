def main():
    prime = [2]
    for i in range(3, 318):
        check = True
        for j in prime:
            check = check and i % j != 0
        if check:
            prime.append(i)
    now = 67
    mas = [-1, -2]
    n = int(input())
    for i in range(2, n + 1):
        for jj in range(66):
            j = prime[jj]
            if i % j == 0:
                print(jj + 1, end=' ')
                break
        else:
            print(now, end=' ')
            now += 1


main()
