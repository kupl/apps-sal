s = lambda: list(map(int, input().split()))

T = int(input())
for tc in range(T):
    n, a, b = s()
    string = list(map(lambda x: x == '1', input()))
    cost = a*n + b*(n+1)
    isBeginning = True
    # state machine
    zeros = 0
    for x in string:
        if x:
            if zeros==0:
                cost+=b
            else:
                if not isBeginning and b*(zeros-1) < 2*a:
                    cost -= 2*a
                    cost += b*(zeros-1)
                isBeginning=False
                zeros=0
                cost+=a+b
        else:
            if zeros==0:
                cost+=a+b
            zeros+=1
    print(cost-a-b) # first number
