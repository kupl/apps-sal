for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    one = l.count(1)
    zero = n-one
    if zero>=n//2:
        print(zero)
        print(*[0]*zero)
    else:
        one -= one%2
        print(one)
        print(*[1]*one)
