try:
    n = int(input())
    stampArr = list(map(int, input().split()))
    nsum = sum(range(1, n + 1))
    ssum = sum(stampArr)
    if nsum == ssum:
        print("YES")
    else:
        print("NO")
except:
    pass
