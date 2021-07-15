def solve():
    n = int(input())
    sm = (1 + n) * n // 2
    i = 1
    while i <= 1073741824:
        if i <= n:
            sm -= 2*i
        else:
            break
        i *= 2
    print(sm)
t = int(input())
for i in range(t):
    solve()

