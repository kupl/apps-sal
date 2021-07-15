def go():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s = sorted(s, key=lambda x: len(x))
    for i in range(n - 1):
        if s[i] not in s[i + 1]:
            print('NO')
            return
    print('YES')
    for i in range(n):
        print(s[i])

go()

