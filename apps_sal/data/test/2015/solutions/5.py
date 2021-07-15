for tc in range(int(input())):
    a,b,c = list(map(int, input().split()))
    n = a+b+c
    if max(a,b,c) > (n+1)//2:
        print('No')
    else:
        print('Yes')

