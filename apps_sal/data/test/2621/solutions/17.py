q = int(input())
for query in range(q):
    arr = [int(x) for x in input().split()]
    arr2 = [int(x) for x in input().split()]
    n = arr[0]
    m = arr[1]
    k = arr[2]
    pos = True
    for i in range(n - 1):
        l = arr2[i + 1] - arr2[i]
        g = l - k
        t = max(g, -arr2[i])
        m -= t
        if m < 0:
            pos = False
            break
    if pos == False:
        print("NO")
    else:
        print("YES")
