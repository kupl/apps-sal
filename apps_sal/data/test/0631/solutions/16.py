for t in range(int(input())):
    n, m = [int(x) for x in input().split(' ')]
    a = [int(x) for x in input().split(' ')]
    ss = sum(a)
    if(ss == m):
        print("YES")
    else:
        print("NO")
