t = int(input())
for j in range(t):
    n = int(input())
    a = (list(map(int, input().split())))
    a.sort()
    s = set()
    s1 = set(a)
    ans = 0
    l = n
    while l > 0:
        now = a.pop()
        l -= 1
        if now not in s and now % 2 == 0:
            s.add(now)
            ans += 1
            if now // 2 not in s1:
                s1.add(now // 2)
                a.append(now // 2)
                l += 1
    print(ans)
