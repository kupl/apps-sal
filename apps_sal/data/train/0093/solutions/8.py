q = int(input())
t = 1
vis = [0] * 300000
for i in range(q):
    (n, m) = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    arr = 0
    i = 0
    k = 0
    for item in b:
        if vis[item] == t:
            arr += 1
            k -= 1
            continue
        while i < n:
            vis[a[i]] = t
            if a[i] == item:
                arr += 2 * k + 1
                i += 1
                break
            i += 1
            k += 1
    print(arr)
    t += 1
