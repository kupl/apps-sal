for _ in range(int(input())):
    n = int(input())
    o1 = e1 = 0
    for i in list(map(int,input().split())):
        if i%2==1:
            o1+=1
    e1 = n-o1
    o2 = e2 = 0
    m = int(input())
    for i in list(map(int,input().split())):
        if i%2==1:
            o2+=1
    e2 = m-o2
    print(e1*e2 + o1*o2)
