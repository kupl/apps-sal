(n, k) = list(map(int, input().split()))
s = input()
a = [0] * 26
for i in range(n):
    a[ord(s[i]) - 97] = 1
uk = 0
su = 0
while 1:
    if a[uk] == 1:
        su += uk + 1
        uk += 2
        k -= 1
    else:
        uk += 1
    if uk >= 26 or k == 0:
        break
if k == 0:
    print(su)
else:
    print(-1)
