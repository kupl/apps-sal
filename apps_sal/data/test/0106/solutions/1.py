read = lambda: list(map(int, input().split()))
n, m, k = read()
a, b = read()
pa = (a - 1) // (m * k) + 1
fa = ((a - 1) % (m * k)) // k + 1
pb = (b - 1) // (m * k) + 1
fb = ((b - 1) % (m * k)) // k + 1
Tp = min(abs(pa - pb), abs(pa - pb + n), abs(pb - pa + n)) * 15
if pa == pb:
    Tf = min(abs(fa - fb) * 5, abs(fa - fb) + 10)
else:
    cnt1 = min((fa - 1) * 5, (fa - 1) + 10)
    cnt2 = min((fb - 1) * 5, (fb - 1) + 10)
    Tf = cnt1 + cnt2
ans = Tp + Tf
print(ans)

