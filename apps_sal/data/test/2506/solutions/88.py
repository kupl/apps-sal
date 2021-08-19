import numpy as np
(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
na = np.zeros(2 ** 18)
for i in a:
    na[i] += 1
fa = np.fft.fft(na)
c = np.round(np.fft.ifft(fa * fa)).astype(int)
ans = 0
cm = 0
for i in range(2 ** 18 - 1, 1, -1):
    cm += c[i]
    ans += i * c[i]
    if cm > m:
        ans -= i * (cm - m)
    if cm >= m:
        break
print(ans)
