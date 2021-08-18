
def resolve():
    N = int(input())
    A = [int(a) for a in input().split()]
    x = 0
    for a in A[2:]:
        x ^= a
    s = sum(A[:2])
    if s < x or (s ^ x) & 1:
        print(-1)
        return
    d = (s - x) // 2
    a = A[0]
    n = 0
    for i in range(40)[::-1]:
        b, c = (x >> i) & 1, (d >> i) & 1
        if b == c == 1:
            print(-1)
            return
        if b == 0 and c == 1:
            n += 1 << i
    for i in range(40)[::-1]:
        b, c = (x >> i) & 1, (d >> i) & 1
        if b == 1 and c == 0:
            if n + (1 << i) <= a:
                n += 1 << i
    if n > a or n == 0:
        print(-1)
    else:
        print(a - n)


resolve()
