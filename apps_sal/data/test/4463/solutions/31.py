s = list(input())
t = list(input())

s = sorted(s, reverse=False)
t = sorted(t, reverse=True)

result = 'No'
rang = min(len(s), len(t))
for i in range(rang):
    if ord(s[i]) < ord(t[i]):
        result = 'Yes'
        break
else:
    if (s[:rang] == t[:rang]) and len(s) < len(t):
        result = 'Yes'
print(result)
