for _ in range(int(input())):
    (n, s, k) = list(map(int, input().split()))
    a = set(map(int, input().split()))
    if s not in a:
        print(0)
        continue
    (t1, t2) = (1, 1)
    i = s
    ans = []
    while i - t1 >= 1:
        if i - t1 in a:
            t1 += 1
        else:
            ans.append(t1)
            break
    while i + t2 <= n:
        if i + t2 in a:
            t2 += 1
        else:
            ans.append(t2)
            break
    print(min(ans))
