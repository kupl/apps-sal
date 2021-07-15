n = int(input())
x = list(map(int, input().split()))
w = tuple(x)
x.sort()
if x[(n//2)-1] == x[n//2]:
    for i in range(n):
        print(x[n//2])
else:
    for h in w:
        if h <= x[(n//2)-1]:
            print(x[n//2])
        else:
            print(x[(n//2)-1])
