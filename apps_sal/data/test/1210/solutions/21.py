(N, p) = map(int, input().split())
blah = []
for _ in range(N):
    (l, r) = map(int, input().split())
    lp = (l + p - 1) // p
    rp = r // p
    count = rp - lp + 1
    blah.append(count / (r - l + 1))
total = 0
for i in range(-1, N - 1):
    (a, b) = (blah[i], blah[i + 1])
    total += a + b - a * b
print(total * 2000)
