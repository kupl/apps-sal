for i in range(int(input())):
    n = int(input())
    s = input()
    odd = 0
    even = 0
    for i in range(0, n, 2):
        if int(s[i]) % 2 == 1:
            odd += 1
    for i in range(1, n, 2):
        if int(s[i]) % 2 == 0:
            even += 1
    if n % 2 == 1:
        if odd > 0:
            print(1)
        else:
            print(2)
    else:
        if even > 0:
            print(2)
        else:
            print(1)
