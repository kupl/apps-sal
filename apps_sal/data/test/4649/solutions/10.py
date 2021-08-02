R = lambda: map(int, input().split())
for _ in range(int(input())):
    n, k = R()
    s = input()
    p = (k + 2) // 2
    l = "RGB" * p
    res = n
    for i in range(n - k + 1):
        c = 0
        # print(l[0:k])
        for j in range(0, k):
            c += (s[i + j] != l[j])
        res = min(res, c)
        # print(c)
        c = 0
        # print(l[1:k+1])
        for j in range(1, k + 1):
            c += (s[i + j - 1] != l[j])
        res = min(res, c)
        # print(c)
        c = 0
        # print(l[2:k+2])
        for j in range(2, k + 2):
            c += (s[i + j - 2] != l[j])
        res = min(res, c)
        # print(c)
    print(res)
