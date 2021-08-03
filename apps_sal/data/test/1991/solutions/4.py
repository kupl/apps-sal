def solve():
    n = int(input())
    a = list(map(int, input().split()))
    i = 0
    ans = 0
    while i < n:
        if a[i] == i + 1:
            i += 1
            continue
        j = i
        while j < n and a[j] != j + 1:
            j += 1
        ans += 1
        i = j
    print(min(ans, 2))


t = int(input())
for _ in range(t):
    solve()
