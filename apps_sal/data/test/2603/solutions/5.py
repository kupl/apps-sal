for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    cur = min(a);
    b = sorted(a);
    good = 1
    
    for i in range(n):
        if (a[i] != b[i] and a[i]%cur > 0):
            good = 0;
    
    if good:
        print("YES")
    else:
        print("NO")

