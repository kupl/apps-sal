n = int(input())
for _ in range(n):
    (c, sn) = map(int, input().split())
    m = sn // c
    b = sn % c
    ans = (m + 1) * (m + 1) * b + m * m * (c - b)
    print(ans)
