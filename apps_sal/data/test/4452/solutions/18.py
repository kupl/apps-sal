t = int(input())
for tests in range(t):
    n = input()
    x = len(n)
    print(x - n.count('0'))
    for i in range(x):
        if n[i] != '0':
            print(n[i] + '0'* (x - i - 1), end =' ')
    print()

