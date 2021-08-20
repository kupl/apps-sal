for _ in range(int(input())):
    (n, k) = tuple(map(int, input().split()))
    s = list(input())
    ans = list('()' * (k - 1) + '(' * (n // 2 - k + 1) + ')' * (n // 2 - k + 1))
    ops = []
    i = 0
    while ans != s and i < n:
        if ans[i] != s[i]:
            j = s[i:].index(ans[i]) + i
            ops.append(str(i + 1) + ' ' + str(j + 1))
            for k in range(i, (j + i + 1) // 2):
                (s[k], s[j + i - k]) = (s[j + i - k], s[k])
        i += 1
    print(len(ops))
    if len(ops) != 0:
        print('\n'.join(ops))
