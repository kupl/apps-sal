n = int(input())
a = input()
b = input()
ans = 0
if n % 2 == 1 and a[n // 2] != b[n // 2]:
    ans += 1
for i in range(0, (n // 2)):
    s = sorted([a[i], a[n - 1 - i], b[i], b[n - 1 - i]])
    l = len(set(s))
    if l == 4:
        ans += 2
    if l == 3:
        if a[i] == a[n - 1 - i]:
            ans += 2
        else:
            ans += 1
    if l == 2:
        if s.count(s[0]) != 2:
            ans += 1
print(ans)
