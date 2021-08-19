t = int(input())


def m(n):
    s = [int(i) for i in str(n)]
    s.sort()
    return (s[0], s[-1])


for _ in range(t):
    (n, k) = map(int, input().split())
    pre = n
    for i in range(2, k + 1):
        a = m(n)
        n = n + a[0] * a[1]
        if pre == n:
            break
        else:
            pre = n
    print(n)
