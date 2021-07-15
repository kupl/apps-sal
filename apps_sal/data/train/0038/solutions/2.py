for i in range(int(input())):
    n, k1, k2 = map(int,input().split())
    l1 = list(map(int,input().split()))
    a = max(l1)
    l2 = list(map(int,input().split()))
    b = max(l2)
    if a > b:
        print("YES")
    else :
        print("NO")
