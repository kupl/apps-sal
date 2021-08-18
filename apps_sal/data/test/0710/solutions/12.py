n = int(input())
s = input()
ans = 10 ** 10
for i in range(len(s) - 3):
    p = 0
    a = abs(ord(s[i]) - ord('A'))
    a = min(a, 26 - a)
    p += a
    a = abs(ord(s[i + 1]) - ord('C'))
    a = min(a, 26 - a)
    p += a
    a = abs(ord(s[i + 2]) - ord('T'))
    a = min(a, 26 - a)
    p += a
    a = abs(ord(s[i + 3]) - ord('G'))
    a = min(a, 26 - a)
    p += a
    ans = min(p, ans)
print(ans)
