for i in range(int(input())):
    n=int(input())
    s=list(map(int,input().split()))
    a=0
    for i in s:
        if i<2049:a+=i
    if a<2048:print("NO")
    else:print("YES")
