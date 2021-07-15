#28 B - Two Anagrams
s = list(input())
t = list(input())

s = sorted(s,reverse = False)
t = sorted(t,reverse = True)

result = 'No'
rang = min(len(s),len(t))
for i in range(rang):
    if ord(s[i]) < ord(t[i]):
        result = 'Yes'
        break
else:
    # 文字が一緒で t の方が文字数が多いとき
    if (s[:rang] == t[:rang]) and len(s) < len(t):
        result = 'Yes'
print(result)
