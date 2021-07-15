def read():
    return list(map(int,input().split()))

q = int(input())
for test in range(q):
    n = int(input())
    a = read()
    a.sort()
    for i in range(n-1):
        if abs(a[i] - a[i+1]) == 1:
            print(2)
            break
    else:
        print(1)

