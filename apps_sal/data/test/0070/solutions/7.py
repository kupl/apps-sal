s = input().split()
n = s[0]
k = int(s[1])

ans = 0
cur = 0
for i in n[::-1]:
    if i == '0':
        cur += 1
    elif cur < k:
        ans += 1
if n.count('0') < k:
    if n.count('0') > 0:
        print(len(n) - 1)
    else:
        print(len(n))
else:
    print(ans)


