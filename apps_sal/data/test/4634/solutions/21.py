t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    i = 0
    j = n - 1
    while i < n and l[i] == 0:
        i += 1
    while j >= 0 and l[j] == 0:
        j -= 1
    ans = 0
    while i <= j:
        if l[i] == 0:
            ans += 1
        else:
            pass
        i += 1
    print(ans)
