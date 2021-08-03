q = int(input())
for _ in range(q):
    k = int(input())
    a = list(map(int, input().split()))
    a = sorted(a, reverse=True)
    ans = 0
    for i in range(k):
        if i + 1 <= a[i]:
            ans = i + 1
    print(ans)
