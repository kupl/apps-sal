def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) ]))
def invr():
    return(list(map(int,input().split())))

n = inp()

for i in range(n):
    n = inp()

    if(n == 1):
        print(0)
    else:
        t = 2
        cnt = 0
        while(n%2 == 0):
            cnt += 1
            n //= 2

        t = 3
        cnt2 = 0
        while(n%3 == 0):
            cnt2 += 1
            n //= 3
        if(cnt2 == 0 or n != 1 or cnt > cnt2):
            print(-1)
        else:
            print(cnt2 - cnt + cnt2)

