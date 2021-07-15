n = int(input())
s = list(input())
glas = list('aoiyue')
f = 1
while f:
    f = 0
    for i in range(1, len(s)):
        if s[i] in glas and s[i - 1] in glas:
            f = 1
            s = s[:i] + s[i + 1:]
            break
print(''.join(s))
