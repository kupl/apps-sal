n = int(input())
x = 4 * n

def is_square(m):
    x = 1
    for i in range(100):
        x = 0.5 * (x + m / x)
    x = int(x)
    if x * x == m:
        return x
    else:
        return -1

ans = -1
for s in range(9 * 18):
    d = s ** 2 + x
    root = is_square(d)
    if root != -1:
        val = -s + root
        if val % 2 == 0 and (val // 2 < ans or ans == -1) and sum(list(map(int, str(val // 2)))) == s:
            ans = val // 2
if ans == -1:
    print(-1)
else:
    print(ans)


