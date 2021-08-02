MOD = 10**9 + 7
I = lambda: list(map(int, input().split()))

n, = I()
l = I()
ans = MOD
for i in range(n):
    x = l[i]
    c = 0
    for i in l:
        c += abs(x - i) % 2
    ans = min(ans, c)
print(ans)
