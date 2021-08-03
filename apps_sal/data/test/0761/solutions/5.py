# Problem D: Slime

n = int(input())

a = input().split()

for i in range(n):
    a[i] = int(a[i])

if(n == 1):
    print(a[0])  # Obvious Case
else:
    sm = 0
    havePositive = False
    haveNegative = False

    for c in a:
        if(c == 0):
            haveNegative = True
            havePositive = True
        elif(c > 0):
            havePositive = True
            sm += c
        else:
            haveNegative = True
            sm -= c

    if(haveNegative and havePositive):
        print(sm)  # Final Answer
    else:
        for i in range(n):
            a[i] = abs(a[i])
        # Get the minimum
        ans = sum(a)
        low = a[0]
        for c in a:
            low = min(low, c)
        # Final Answer
        print(ans - 2 * low)
