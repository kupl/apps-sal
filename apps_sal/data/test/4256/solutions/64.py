A,B,C = map(int,input().split())

if A > B:
    print('0')
elif B // A >= C:
    print(C)
elif B // A < C:
    print(B // A)
