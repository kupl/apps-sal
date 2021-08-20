s = input()
su = sum(map(int, list(s)))
while len(s) > 0 and s[-1] == '9':
    s = s[:-1]
print(su + 9 * max(0, len(s) - 1))
