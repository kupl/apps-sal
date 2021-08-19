T = int(input())
for _ in range(T):
    (n, k) = list(map(int, input().split()))
    c = list(map(int, input().split()))
    a = []
    for i in c:
        a.append(i - 1)
    b = [-1] * n
    for i in range(n):
        m = 300
        for j in a:
            m = min(abs(i - j) + 1, m)
        b[i] = m
    print(max(b))
