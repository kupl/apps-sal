for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    s=0
    for i in arr:
        if i<=2048:
            s+=i
    if s>=2048:
        print("YES")
    else:
        print("NO")


