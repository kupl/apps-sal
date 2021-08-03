for _ in range(int(input())):
    n = int(input())
    s = input()
    if n % 2 == 1:
        a = [int(i) % 2 for i in s[::2]]
        if 1 in a:
            print(1)
        else:
            print(2)
    else:
        a = [int(i) % 2 for i in s[1::2]]
        if 0 in a:
            print(2)
        else:
            print(1)
