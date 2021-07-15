A,B= map(int, input().split())

if A + B >= A - B:
    if A + B >= A * B:
        print(A+B)
    else:
        print(A*B)
elif A-B >= A*B:
    print(A-B)
else:
    print(A*B)
