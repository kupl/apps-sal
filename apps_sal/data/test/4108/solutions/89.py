s = input()
t = input()
memo = {}
ans = 'Yes'
for i in range(len(s)):
    if s[i] in memo:
        if t[i] != memo[s[i]]:
            ans = 'No'
            break
    else:
        memo[s[i]] = t[i]
a = list(memo.values())
b = list(set(a))
if len(b) != len(a):
    ans = 'No'
print(ans)
