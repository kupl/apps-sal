# cook your dish heretry
try:
    n = int(input())
    l = [int(x) for x in input().split()]
    if((n * (n + 1) // 2) == sum(l)):
        print("YES")
    else:
        print("NO")
except:
    pass
