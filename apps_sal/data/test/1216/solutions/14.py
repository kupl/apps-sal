n = input()
s = input()
i = 0
t = ""
while i < int(n):
    if (i == 0 or s[i] != s[i - 1] or (s[i] != 'a' and s[i] != 'e' and s[i] != 'i' and s[i] != 'o' and s[i] != 'u' and s[i] != 'y') or (s[i] == s[i - 1] and ((s[i] == 'e' or s[i] == 'o') and (i < 2 or s[i - 2] != s[i]) and (i + 1 == int(n) or s[i + 1] != s[i])))):
        t += s[i]
    i = i + 1
print(t)
