for _ in range(int(input())):
    print(pow(2, bin(int(input())).count('1')))
