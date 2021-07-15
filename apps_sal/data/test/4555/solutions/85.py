a, b, k = map(int,input().split())
if a+k+1 <= b:
    for i in range(a, k+a):
        print(i)
    if a+k+1 <= b+1-k:
        for i in range(b+1-k, b+1):
            print(i)
    else:
        for i in range(a+k, b+1):
            print(i)
else:
    for i in range(a, b+1):
        print(i)
