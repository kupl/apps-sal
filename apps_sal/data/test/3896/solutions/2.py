s = input()
ans = 0
for i, c in enumerate(s):
    if c == '1':
        ans += 1 << (2 * len(s) - i - 2)
print(ans % (10 ** 9 + 7))
