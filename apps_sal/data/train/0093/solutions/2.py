t = int(input())
for _ in range(t):
    (n, m) = list(map(int, input().split(' ')))
    a = list(map(int, input().split(' ')))
    b = list(map(int, input().split(' ')))
    order = [0] * (n + 1)
    for i in range(n):
        order[a[i]] = i
    pref_max = 0
    ans = 0
    for i in range(m):
        if order[b[i]] < pref_max:
            ans += 1
        else:
            pref_max = order[b[i]]
            ans += 2 * (order[b[i]] - i) + 1
    print(ans)
