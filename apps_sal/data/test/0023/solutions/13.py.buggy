def check(m):
    nonlocal c, ans
    ans = [0] * len(a)
    have = c[:]
    for i in range(m):
        if have[b[i]] > 0:
            have[b[i]] -= 1
            ans[i] = b[i]
        else:
            return 0
    for i in range(b[m] - 1, -1, -1):
        if have[i]:
            ans[m] = i
            have[i] -= 1
            break
    else:
        return 0
    j = m + 1
    for i in range(10, -1, -1):
        for t in range(have[i]):
            ans[j] = i
            j += 1
    return (j == len(a))


a = list(map(int, list(input())))
b = list(map(int, list(input())))
ans = [0] * len(a)

if len(a) < len(b):
    a.sort(reverse=1)
    for i in a:
        print(i, end='')
    print()
else:
    a.sort(reverse=1)
    if a == sorted(b, reverse=1):
        for i in b:
            print(i, end='')
        print()
    else:
        c = [0] * 15
        for i in a:
            c[i] += 1

        for i in range(len(a) - 1, -1, -1):
            if check(i):
                for i in ans:
                    print(i, end='')
                print()
                break
        else:
            for i in b:
                print(i, end='')
            print()
