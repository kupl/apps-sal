t = int(input())
for i in range(t):
    n, x = list(map(int, input().split()))
    a = list(map(int, input().split()))
    j = 0
    ind = 1
    while j <= x:
        if ind not in a:
            if j == x:
                break
            j += 1
        ind += 1
    print(ind - 1)

