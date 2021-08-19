s = str(input())


def ispalindrome(s):
    if s == s[::-1]:
        return True
    return False


for i in range(len(s) + 1):
    if i < len(s) / 2:
        t = s[:i] + s[len(s) - i - 1] + s[i:]
    else:
        t = s[:i] + s[len(s) - i] + s[i:]
    if ispalindrome(t):
        print(t)
        quit()
print('NA')
