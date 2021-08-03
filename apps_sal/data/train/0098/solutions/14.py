q = int(input())
for _ in range(q):
    c, m, x = list(map(int, input().split()))
    s = c + m + x
    i = min(c, m)
    if s // 3 <= i:
        print(s // 3)
    else:
        print(min(i, s - i * 2))
