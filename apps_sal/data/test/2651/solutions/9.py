(n, m) = map(int, input().split())
lists = list(map(int, input().split()))
sub = list(map(int, input().split()))
mod = 10 ** 9 + 7
tate = 0
yoko = 0
for i in range(n):
    tate += lists[i] * (2 * (i + 1) - 1 - n)
for j in range(m):
    yoko += sub[j] * (2 * (j + 1) - 1 - m)
print(tate % mod * (yoko % mod) % mod)
