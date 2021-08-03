t = int(input())
for _ in range(t):
    s = input()
    a = [i for i in s]
    c = ['a', 'b', 'c']
    ok = True
    if len(s) == 1:
        if s == '?':
            print('a')
        else:
            print(s)
    else:
        for i in range(len(s) - 1):
            if a[i] is not '?':
                if a[i] == a[i + 1]:
                    ok = False
        if ok:
            for i in range(len(s)):
                if a[i] == '?':
                    if i == 0:
                        for j in c:
                            if j is not a[i + 1]:
                                a[i] = j
                                break
                    elif i == len(s) - 1:
                        for j in c:
                            if j is not a[i - 1]:
                                a[i] = j
                                break
                    else:
                        for j in c:
                            if j is not a[i - 1] and j is not a[i + 1]:
                                a[i] = j
                                break
            ok = True
            for i in range(len(s) - 1):
                if a[i] == a[i + 1]:
                    ok = False
                    break
            if ok:
                print("".join(a))
            else:
                print(-1)

        else:
            print(-1)
