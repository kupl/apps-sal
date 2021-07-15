for _ in range(int(input())):
    n = int(input())
    a = sorted([int(i) for i in input().split()])
    k = min(a[-1]-1,a[-2]-1,len(a)-2)
    print(k)


