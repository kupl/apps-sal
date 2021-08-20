def vowel(t):
    if t == 'a' or t == 'e' or t == 'i' or (t == 'o') or (t == 'u') or (t == 'y'):
        return True
    else:
        return False


n = int(input())
s = input()
cur = 1
vow = vowel(s[0])
while cur < len(s):
    preVow = vow
    vow = vowel(s[cur])
    if preVow and vow:
        s = s[:cur] + s[cur + 1:]
    else:
        cur += 1
print(s)
