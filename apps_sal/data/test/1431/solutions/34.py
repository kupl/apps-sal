n = int(input())
b = list(map(int, input().split()))
a = [0] * (n + 1)
for i in range(1, n + 1):
    a[i] = b[i - 1]


ball = [0] * (n + 1)
ans = []

for i in range(n, 0, -1):
    s = 0
    j = i * 2
    while j <= n:
        s += ball[j]
        j += i

    if s % 2 != a[i]:
        ball[i] += 1
        ans.append(i)

print((len(ans)))
for e in ans:
    print(e)

