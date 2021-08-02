n, m = list(map(int, input().split()))
nt = n // 5
mt = m // 5

nf = [nt] * 5
mf = [mt] * 5

for x in range((n % 5) + 1):
    nf[x] += 1

for x in range((m % 5) + 1):
    mf[x] += 1

nf[0] -= 1
mf[0] -= 1

ans = 0
for x in range(5):
    y = (5 - x) % 5
    ans += nf[x] * mf[y]

print(ans)
