
def f(): return input()


n, m = list(map(int, f().split()))

cc = [0] * (n + 1)
for i in range(m):
    a, b = list(map(int, f().split()))
    cc[a] += 1
    cc[b] += 1

center = 0
for i in range(1, n + 1):
    if cc[i] == 0:
        center = i
        break

print(n - 1)

for i in range(1, n + 1):
    if i != center:
        print(i, center)
