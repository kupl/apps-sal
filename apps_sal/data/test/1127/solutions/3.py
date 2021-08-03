t = int(input())
for you in range(t):
    n = int(input())
    s = input()
    if(n % 2 == 0):
        poss = 0
        for i in range(1, n, 2):
            if(int(s[i]) % 2 == 0):
                poss = 1
                break
        if(poss):
            print(2)
        else:
            print(1)
    else:
        poss = 0
        for i in range(0, n, 2):
            if(int(s[i]) % 2 == 1):
                poss = 1
                break
        if(poss):
            print(1)
        else:
            print(2)
