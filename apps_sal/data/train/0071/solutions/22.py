t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    h = 0
    ans = 0
    for j in range(n):
        h += l[j]
        if h < 0:
            ans = max(ans, abs(h))
    print(ans)
