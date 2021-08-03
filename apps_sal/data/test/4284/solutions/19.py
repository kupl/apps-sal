q = int(input())
for i in range(0, q):
    s = input()
    s = s.split()
    k = int(s[0])
    n = int(s[1])
    a = int(s[2])
    b = int(s[3])
    if k - b * n > 0:
        j = (k - b * n - 1) / (a - b)
        if j > n:
            j = n
        print(int(j))
    else:
        print(-1)
