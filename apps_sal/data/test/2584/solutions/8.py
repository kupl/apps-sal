t = int(input())
for ii in range(t):
    (n, p, k) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a = sorted(a)
    a = [None] + a
    s = [0] * (n + 1)
    last_ind = 0
    for i in range(1, n + 1):
        if i < k:
            s[i] = a[i] + s[i - 1]
        else:
            s[i] = a[i] + s[i - k]
        if s[i] <= p:
            last_ind = i
    print(last_ind)
'\n8\n5 6 2\n2 4 3 5 7\n5 11 2\n2 4 3 5 7\n3 2 3\n4 2 6\n5 2 3\n10 1 3 9 2\n2 10000 2\n10000 10000\n2 9999 2\n10000 10000\n4 6 4\n3 2 3 2\n5 5 3\n1 2 2 1 2\n\n'
