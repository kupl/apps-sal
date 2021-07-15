
for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    s=sum(a)
    if s==0:
        print("NO")
    else:
        print("YES")
        if s>0:
            a=a[::-1]
        a=[str(i) for i in a]
        print(" ".join(a))

