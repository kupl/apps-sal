import string

n, m = map(int, input().split())
s = input()

chars = string.ascii_lowercase

for _ in range(m):
    a, b = input().split()
    chars = chars.replace(a, "%").replace(b, a).replace("%", b)

replacements = {ord(string.ascii_lowercase[i]): chars[i] for i in range(26)}

print(s.translate(replacements))
