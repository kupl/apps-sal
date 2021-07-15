n = int(input())
a = list(map(int, input().split()))
s = sum(a)
ans = []
ma, se = 0, 0
for i in range(n):
    if ma < a[i]:
        se = ma
        ma = a[i]
    elif ma == a[i]:
        se = a[i]
    elif se < a[i]:
        se = a[i]

for i in range(n):
    s -= a[i]
    if a[i] == ma:
        if s == se * 2:
            ans.append(i + 1)
        s += a[i]
        continue

    if s == ma * 2:
        ans.append(i + 1)
    s += a[i]

print(len(ans))
print(" ".join(map(str, ans)))
