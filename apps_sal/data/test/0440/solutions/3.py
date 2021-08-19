n = int(input())
s = input()
i = 0
while i < len(s):
    if i < len(s) - 1 and s[i + 1] in 'aeyuio' and (s[i] in 'aeyuio'):
        s = s[:i + 1] + s[i + 2:]
        i -= 1
    i += 1
print(s)
