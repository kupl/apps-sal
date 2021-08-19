p = input()
l = len(p) - 1
ans = ''
s = ['23', '10', '30', '11', '13', '12', '31', '33', '32', '21']
for x in p:
    ans += s[ord(x) - 48]
if ans == ans[::-1]:
    print('Yes')
else:
    print('No')
