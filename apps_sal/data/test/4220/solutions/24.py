k = int(input())
s = input()
ans = ''
if len(s) <= k:
    print(s)
else:
    for i in range(k):
        ans += s[i]
    print(ans + '...')
