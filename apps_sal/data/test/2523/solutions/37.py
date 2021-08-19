s = input()
"\ns = '101'\ns = '100000000'\ns = '00001011'\n"
k = len(s)
for i in range(1, len(s)):
    if s[i - 1] != s[i]:
        k = min(k, max(i, len(s) - i))
print(k)
