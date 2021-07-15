n = int(input())
for i in range(n):
    x = input()
    print(9 * (len(str(x)) - 1) + int(x) // int('1' * len(x)))


