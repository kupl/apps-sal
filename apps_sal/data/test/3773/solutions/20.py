(A, I) = (0, input)
for i in range(int(I())):
    (a, k) = map(int, I().split())
    g = 0
    while 1:
        if a < k:
            g = 0
            break
        if a % k == 0:
            g = a // k
            break
        c = (a // k + a % k) // (a // k + 1)
        a -= c * (a // k + 1)
    A ^= g
print('Takahashi' if A else 'Aoki')
