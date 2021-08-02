tests = int(input())
for _ in range(tests):
    s = input()
    n = int(input())
    b = list(map(int, input().split()))
    g = sorted(b)
    ans = ['a'] * n
    d = dict()
    for i in set(s):
        d[i] = 0
    for i in s:
        d[i] += 1
    tec = 122
    r = b.count(0)
    while r != 0:
        flag = True
        while flag:
            if chr(tec) in d:
                if d[chr(tec)] >= r:
                    flag = False
                    break
            tec -= 1
        sp = []
        for i in range(n):
            if b[i] == 0:
                sp.append(i)
                b[i] = -1
        for i in range(n):
            summ = 0
            if b[i] < 0:
                continue
            for j in sp:
                summ += abs(i - j)
            b[i] -= summ
        for i in sp:
            ans[i] = chr(tec)
        tec -= 1
        r = b.count(0)
    for i in ans:
        print(i, end='')
    print()
