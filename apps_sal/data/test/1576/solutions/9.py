s = str(input())
a = []
for i in range(0, len(s)):
    a += [s[i]]
if len(a) % 2 == 0:
    k = -1
else:
    k = 0
ans = ''
while len(a) > 0:
    ans += a[k]
    del a[k]
    if k == -1:
        k = 0
    else:
        k = -1
print(ans[::-1])
