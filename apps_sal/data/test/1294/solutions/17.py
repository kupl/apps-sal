n = int(input())

while(n):
    
    S = input()
    S += "_"
    lastChar = ""
    cur = 0
    x = set()
    for s in S:
        if s != lastChar:
            if cur % 2:
                x.add(lastChar)
            lastChar = s
            cur = 1
        else:
            cur += 1
    
    x = list(x)
    x.sort()
    for c in x:
        print(c, end='')
    print()
    
    n -= 1
