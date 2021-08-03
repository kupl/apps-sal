n = int(input())
a = list(map(int, input().split()))
d = [0 for i in range(n + 1)]
ans = [0 for i in range(n + 1)]
for i in range(n, 0, -1):
    c = 0
    for j in range(i * 2, n + 1, i):
        c += ans[j]
    if (c % 2) ^ a[i - 1]:
        ans[i] = 1

r = ""
c = 0
for i in range(1, n + 1):
    if ans[i]:
        c += 1
        r += str(i) + " "
print(c)
print((r[:-1]))
