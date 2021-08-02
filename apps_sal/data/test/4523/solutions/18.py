for _ in range(int(input())):
    n = int(input())
    #n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    s = 1
    for i in range(n - 1):
        if(abs(a[i] - a[i + 1]) > 1):
            s = 0
    if(s == 1):
        print("YES")
    else:
        print("NO")
