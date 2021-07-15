k = int(input())
s = str(input())

if len(s) <= k:
    print(s)
else:
    ans = s[0:k] + '...'
    print(ans)
