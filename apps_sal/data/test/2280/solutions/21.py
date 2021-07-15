q = int(input())
for i in range(q):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    ans = 0
    for i in range(n - 2):
        if (ans + 1 == l[-2]):
            break
        else:
            ans += 1
    print(ans)
