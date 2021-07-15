for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    oa, ea, ob, eb = 0, 0, 0, 0
    for i in a:
        if i%2:
            oa+=1
        else:
            ea+=1
    for i in b:
        if i%2:
            ob+=1
        else:
            eb+=1
    print(oa*ob + ea*eb)
