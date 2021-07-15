t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    if n % 2 == 0:
        for i in range(1, n, 2):
            if int(s[i]) % 2 == 0:
                print(2)
                break
        else:
            print(1)
    else:
        for i in range(0, n, 2):
            if int(s[i]) % 2 == 1:
                print(1)
                break
        else:
            print(2)

