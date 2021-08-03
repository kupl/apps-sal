def ispal(s):
    if s == s[::-1]:
        return True
    else:
        return False


s = str(input())
if ispal(list(s)):
    print("YES")
    return
l = list(s)
while l[-1] == '0':
    l = l[:-1]
if ispal(l):
    print("YES")
else:
    print("NO")
