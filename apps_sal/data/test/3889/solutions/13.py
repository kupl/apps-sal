n = int(input())
s = input()
num = [0] * 26
if n == 1:
    print('Yes')
else:
    for i in range(len(s)):
        num[ord(s[i]) - 97] += 1
    fl = False
    for i in range(26):
        if num[i] > 1:
            fl = True
            break
    if fl:
        print('Yes')
    else:
        print('No')
