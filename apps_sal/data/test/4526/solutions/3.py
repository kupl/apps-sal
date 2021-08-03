t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    p = max(s)
    dict = {}
    for i in range(n):
        count = s[i]
        for j in range(i + 1, n):
            count += s[j]
            dict[count] = 1
            if count >= p:
                break
    ans = 0
    for i in range(n):
        if dict.get(s[i]) is not None:
            ans += 1
    print(ans)
