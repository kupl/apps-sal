def inv_mod(a, p=10**9+7):
    p = abs(p)
    a %= p
    stack = []
    p0 = p
    while a > 1:
        d, a, p = p//a, p%a, a
        stack.append(d)
    x, y = 1, 0
    while stack:
        d = stack.pop()
        x, y = y-d*x, x
    return x % p0

MOD = 10**9 + 7
inpl = lambda: list(map(int,input().split()))
N = int(input())
a = ord(input()) - ord('A')
b = ord(input()) - ord('A')
c = ord(input()) - ord('A')
d = ord(input()) - ord('A')
if N == 2 or N == 3:
    print((1))
    return
if b == 0:
    a, b, c, d = 1-d, 1-b, 1-c, 1-a

if d == 1:
    print((1))
elif c == 0:
    print((pow(2, N-3, MOD)))
else: # (d, c) = (0, 1)
    n = N - 3
    cur = 1
    ans = cur
    for k in range((n+1)//2):
        cur *= (n-2*k)*(n-2*k+1)*inv_mod(k+1)*inv_mod(n-k+1)
        cur %= MOD
        ans += cur
        ans %= MOD
    print(ans)

