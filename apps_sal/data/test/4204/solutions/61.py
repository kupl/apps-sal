s = input()
k = int(input())
s1 = 0
sn1 = '0'
for i in range(len(s)):
    if s[i] == '1':
        s1 += 1
    else:
        sn1 = s[i]
        break
ans = '0'
if s1 >= k:
    ans = '1'
else:
    ans = sn1
print(ans)
