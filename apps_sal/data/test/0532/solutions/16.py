import string
s = input()
a = 'a'
ans = 0
for c in s:
    i = string.ascii_lowercase.index(c) - string.ascii_lowercase.index(a)
    i = abs(i)
    i = min(i, 26 - i)
    a = c
    ans += i
print(ans)
