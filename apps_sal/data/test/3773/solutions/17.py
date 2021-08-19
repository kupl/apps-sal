N = int(input())
res = 0
for i in range(N):
    (n, k) = list(map(int, input().split()))
    while n % k != 0 and n // k > 0:
        q = n // k
        r = n % k
        R = r % (q + 1)
        if r > q + 1:
            n = q * k + R
        else:
            n = q * k + r - (q + 1)
    if n % k == 0:
        res ^= n // k
if res == 0:
    print('Aoki')
else:
    print('Takahashi')
