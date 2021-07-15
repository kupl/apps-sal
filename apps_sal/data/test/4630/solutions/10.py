def read():
    return list(map(int,input().split()))

q = int(input())
for test in range(q):
    n = int(input())
    a = read()
    for i in range(n):
        a[i] -= 1
    used = [False]*n
    ans = [0]*n
    for i in range(n):
        if not used[i]:
            j = a[i]
            k = 1
            while j!=i:
                k += 1
                j = a[j]
            j = a[i]
            ans[i] = k
            while j!=i:
                j = a[j]
                ans[j] = k
                used[j] = True
    print(*ans)

