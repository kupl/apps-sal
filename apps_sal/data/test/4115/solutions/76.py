def resolve():
    s = input()
    n = len(s)
    a = s[:n // 2]
    b = s[::-1][:n // 2]
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
    print(cnt)


resolve()
