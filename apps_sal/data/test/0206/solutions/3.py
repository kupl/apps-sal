M, a, b = map(int, input().split())
mod = 10**9 + 7
D = [mod] * a
maxi = 0
D[0] = 0
Q = [0]


def f(x, i):
    t = (x + 1 - i) // a
    r = (x + 1 - i) % a
    return a * t * (t + 1) // 2 + r * (t + 1)


while Q:
    q = Q.pop()
    D[q] = maxi
    k = max(0, -((-(b - q)) // a))
    maxi = max(maxi, q + k * a)
    if D[(q - b) % a] == mod and maxi <= M:
        Q.append((q - b) % a)
ans = 0
for i, d in enumerate(D):
    if d > M:
        continue
    ans += f(M, i) - f(d - 1, i)
print(ans)
