s = input().split()
s.sort()
if s[0] == s[1] == s[2]:
    print(0)
    return
if s[0][1] == s[1][1] == s[2][1]:
    if ord(s[0][0]) + 1 == ord(s[1][0]) == ord(s[2][0]) - 1:
        print(0)
        return
if s[0][1] == s[1][1] and ord(s[0][0]) + 2 >= ord(s[1][0]) or s[1][1] == s[2][1] and ord(s[1][0]) + 2 >= ord(s[2][0]) or s[0][1] == s[2][1] and ord(s[0][0]) + 2 >= ord(s[2][0]):
    print(1)
    return
if s[0] == s[1] or s[1] == s[2] or s[0] == s[2]:
    print(1)
    return
print(2)
