N = int(input())
a = list(map(int, input().split()))

max1 = max(a)
min1 = min(a)

if min1 >= 0:
    print(N-1)
    for i in range(N-1):
        print(i+1, i+2)
elif max1 <= 0:
    print(N-1)
    for i in range(N-1):
        print(N-i, N-i-1)
else:
    if -min1 < max1:
        t = a.index(max1) + 1
        print(2*N - 1)
        for i in range(N):
            print(t, i+1)
        for i in range(N-1):
            print(i+1, i+2)
    else:
        t = a.index(min1) + 1
        print(2*N - 1)
        for i in range(N):
            print(t, i+1)
        for i in range(N-1):
            print(N-i, N-i-1)
