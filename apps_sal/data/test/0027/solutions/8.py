def test(k):
    if len(s) >= 2 * k:
        return s[:k] == s[k:2 * k]
    return False


n = int(input())
s = input()
d = 0
for i in range(len(s) + 1):
    if test(i):
        d = i
print(min(len(s), len(s) - 2 * d + d + 1))
