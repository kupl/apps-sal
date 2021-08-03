s = input()
now = len(s)
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        now = min(now, max(i + 1, len(s) - i - 1))
print(now)
