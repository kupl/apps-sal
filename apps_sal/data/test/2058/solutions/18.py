a = input()
b = input()
ans = 0
pref = [0 for i in range(len(b) + 1)]
for i in range(len(b)):
    pref[i + 1] = pref[i] + int(b[i])
for i in range(len(a)):
    ans += abs(int(a[i]) * (len(b) - len(a) + 1) - pref[len(b) - len(a) + i + 1] + pref[i])
print(ans)
