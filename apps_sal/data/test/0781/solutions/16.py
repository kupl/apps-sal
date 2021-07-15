def good(s):
    for i in range(7, -1, -1):
        if s[i] == s[i-1]:
            return False
    return True
for i in range(8):
    if not good(input()):
        print('NO')
        return
print('YES')

