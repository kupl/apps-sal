from collections import Counter
n, mod = map(int, input().split())
s = input()
if mod == 2:
    ans = 0
    for i in range(n - 1, -1, -1):
        if int(s[i]) % 2 == 0:
            ans += i + 1
    print(ans)
    return
elif mod == 5:
    ans = 0
    for i in range(n - 1, -1, -1):
        if int(s[i]) % 5 == 0:
            ans += i + 1
    print(ans)
    return

l = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    l[i] = (l[i + 1] + int(s[i]) * pow(10, n - 1 - i, mod)) % mod
# print(l)
c = Counter(l)
# print(c)


def nC2(i):
    return i * (i - 1) // 2


ans = c[0] - 1 + nC2(c[0] - 1)
for i in range(1, mod):
    ans += nC2(c[i])
print(ans)
