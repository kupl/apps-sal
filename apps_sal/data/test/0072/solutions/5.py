def ct(s):
    a = [0] * 26 * 2
    for i in s:
        if ord(i) < 97:
            a[ord(i) - 65] += 1
        else:
            a[ord(i) - 97 + 26] += 1
    return max(a)


n = int(input())
s1 = input()
ln = len(s1)
s1 = ct(s1)
s2 = ct(input())
s3 = ct(input())
s = [s1, s2, s3]
for i in range(len(s)):
    if s[i] == ln and n == 1:
        s[i] = ln - 1
    else:
        s[i] = s[i] + n
    if s[i] > ln:
        s[i] = ln
s1 = s[0]
s2 = s[1]
s3 = s[2]
s.sort()
if s[2] == s[1]:
    print('Draw')
elif s[-1] == s1:
    print('Kuro')
elif s[-1] == s2:
    print('Shiro')
elif s[-1] == s3:
    print('Katie')
