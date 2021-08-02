a = input()
n = int(a[:-1])
s = a[-1]
ans = ((n - 1) // 4) * 16
n -= ((n - 1) // 4) * 4
d = {'f': 1, 'e': 2, 'd': 3, 'a': 4, 'b': 5, 'c': 6}
if n in (1, 3):
    ans += d[s]
else:
    ans += 7 + d[s]
print(ans)
