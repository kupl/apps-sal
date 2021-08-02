a = input()
b = input()
x = b.count('1') % 2

pref = [0] * (len(a) + 1)
for i in range(len(a)):
    if a[i] == '0':
        pref[i] = pref[i - 1]
    else:
        pref[i] = pref[i - 1] + 1

ans = 0
for i in range(len(a) - len(b) + 1):
    if (pref[i + len(b) - 1] - pref[i - 1]) % 2 == x:
        ans += 1
print(ans)
