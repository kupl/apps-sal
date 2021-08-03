wc = input()
n = len(wc)
w = [wc[i] for i in range(n)]
m = int(input())


cnt = [0 for i in range(n + 3)]
y = [int(x) for x in input().split()]
for i in range(m):
    x = y[i]
    cnt[x] += 1
    cnt[n - x + 2] -= 1

for i in range(n + 1):
    if i > 0:
        cnt[i] += cnt[i - 1]

for i in range(1, n + 1, 1):
    if n - i + 1 <= i:
        break

    if cnt[i] % 2 == 1:
        a = i - 1
        b = n - i
        tmp = w[a]
        w[a] = w[b]
        w[b] = tmp

for i in range(n):
    print(w[i], end="")
print()
