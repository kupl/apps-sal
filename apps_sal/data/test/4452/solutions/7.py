for _ in range(int(input())):
    s = input()
    print(len(s) - s.count('0'))
    n = int(s)
    pw = 1
    while n:
        if n % 10:
            print(pw * (n % 10), end=' ')
        n //= 10
        pw *= 10
    print()
