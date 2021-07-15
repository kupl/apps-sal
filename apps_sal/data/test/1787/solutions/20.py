s = input()
m = 10**9+7
a = []
j = 0
for i in range(len(s)):
    if s[i] == 'b':
        a.append(j)
        j = 0
    elif s[i] == 'a':
        j += 1
if j != 0:
    a.append(j)
if len(a) == 0:
    print(0)
    return

ans = a[0]
for i in range(1, len(a)):
    ans = (ans+ans*a[i]+a[i])%m
print(ans)
