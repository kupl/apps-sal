q = int(input())
p = [True] * 100010
s = [0] * 100010
p[0] = False
p[1] = False
i = 2
while i <= 100005:
    if p[i]:
        j = i * 2
        while j <= 100005:
            p[j] = False
            j += i
    i += 1
for i in range(100005):
    if i & 1 and p[i] and p[(i + 1) // 2]:
        s[i] += 1
for i in range(100005):
    s[i + 1] += s[i]
for _ in range(q):
    (l, r) = list(map(int, input().split()))
    print(s[r] - s[l - 1])
