t = int(input())
for i in range(t):
    n = int(input())
    arr = 0
    a = [int(x) for x in input().split()]
    s = sum(a)
    for item in a:
        if item == 0:
            arr += 1
            s += 1
    if s == 0:
        print(arr + 1)
    else:
        print(arr)
