def mi():
    return list(map(int, input().split()))


'\n4\n8 2 5\n00110010\n8 1 1\n00110010\n9 100000000 100000000\n010101010\n2 5 1\n00\n'
for _ in range(int(input())):
    (n, a, b) = mi()
    s = list(map(int, input()))
    ans = (a + b) * n + b
    if 1 not in s:
        print(ans)
        continue
    i1 = s.index(1)
    i2 = n - 1 - s[::-1].index(1)
    ans += 2 * a + (i2 - i1 + 2) * b
    i = i1
    while i < i2:
        enter = False
        while i < i2 and s[i] == 1:
            enter = True
            i += 1
        start = i
        while i < i2 and s[i] == 0:
            enter = True
            i += 1
        if i < n and s[i] == 1 and (s[i - 1] == 0):
            enter = True
            if 2 * a - b * (i - start - 1) < 0:
                ans += 2 * a - b * (i - start - 1)
        if not enter:
            break
    print(ans)
