a = input()
b = input()
i = b.count('1')
s = [0 for k in range(len(a))]
if a[0] == '1':
    s[0] = 1
for k in range(1, len(a)):
    if a[k] == '1':
        s[k] = s[k - 1] + 1
    else:
        s[k] = s[k - 1]
s = s + [0]
ans = 0
for k in range(len(a) - len(b) + 1):
    t = s[k + len(b) - 1] - s[k - 1]
    if i % 2 == t % 2:
        ans += 1
print(ans)
