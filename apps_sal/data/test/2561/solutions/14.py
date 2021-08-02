for _ in range(int(input())):
    n = int(input())
    print((2**bin(n)[2:].count('1') - 1) + 1)
