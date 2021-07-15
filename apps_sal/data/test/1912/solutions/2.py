mod = 10**9 + 7
def solve():
    r, g, b, w = map(int, input().split())
    ok = False
    for i in range(20):
        if (r % 2 + g % 2 + b % 2 + w % 2) <= 1:
            ok = True
        mn = min(r, g, b, 1)
        r -= mn
        g -= mn
        b -= mn
        w += 3 * mn
    print('Yes' if ok else 'No')
t = 1
t = int(input())
for _ in range(t):
    solve()
