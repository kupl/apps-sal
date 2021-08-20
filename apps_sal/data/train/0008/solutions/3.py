for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    s = input()
    k = min(k, s.count('L'))
    arr = []
    cur = 0
    sc = 0
    se = False
    if s[0] == 'W':
        sc += 1
    for e in s:
        if e == 'L':
            cur += 1
        else:
            if cur > 0 and se:
                arr.append(cur)
            se = True
            cur = 0
    for i in range(1, n):
        if s[i] == 'W':
            if s[i - 1] == 'W':
                sc += 2
            else:
                sc += 1
    arr.sort()
    arr.reverse()
    while len(arr) > 0 and arr[-1] <= k:
        k -= arr[-1]
        sc += arr[-1] * 2 + 1
        arr.pop()
    sc += k * 2
    if k > 0 and s.count('W') == 0:
        sc -= 1
    print(sc)
