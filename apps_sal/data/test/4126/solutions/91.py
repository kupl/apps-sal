def isParindrome(s):
    return s == s[::-1]

string = input()

ans = True
if not isParindrome(string):
    ans = False
if not isParindrome(string[(len(string)+1)//2:]):
    ans = False
if ans:
    print('Yes')
else:
    print('No')
