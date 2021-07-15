s = input().strip()
s1 = str(''.join(list(reversed(s))))
while len(s1) < 100 and s1 != s:
    s1 += '0'
    s = '0' + s
if s == s1:
    print("YES")
else:
    print("NO")
