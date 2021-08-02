# cook your dish here
s = input().strip()
d = 0
cur = 0
# print(s)
for i in range(len(s) - 1):
    for j in range(i + 1, len(s)):
        if s[i] != s[j]:
            cur = j - i
    d = max(d, cur)

print(d)
