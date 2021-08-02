import string
n = int(input())
s = input()
sm = string.ascii_lowercase
b = string.ascii_uppercase
ans = 0
h = set()
for i in range(len(s)):
    if s[i] in sm:
        h.add(s[i])
        ans = max(ans, len(h))
    else:
        h = set()
print(ans)
