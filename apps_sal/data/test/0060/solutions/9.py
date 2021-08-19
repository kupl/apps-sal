s = input()
n = int(s[:len(s) - 1])
n -= 1
ans = n // 4 * 16
n %= 4
if n % 2 == 1:
    ans += 6 + 1
d = {'a': 4, 'f': 1, 'e': 2, 'd': 3, 'b': 5, 'c': 6}
print(ans + d[s[-1]])
