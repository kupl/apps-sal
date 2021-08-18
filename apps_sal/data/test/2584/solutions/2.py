

q = int(input())
for _ in range(q):
    n, p, k = map(int, input().split(' '))
    a = list(map(int, input().split(' ')))

    a.sort()

    m = 0
    for i in range(k):
        c = 0
        tmp = -1
        if i > 0:
            tmp = i - 1
            c = a[tmp]

        while p >= c:
            tmp = tmp + k
            if tmp >= n:
                break
            c = c + a[tmp]

        if tmp + 1 - k > m:
            m = tmp + 1 - k

    print(m)
