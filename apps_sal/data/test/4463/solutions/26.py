#28 B - Two Anagrams AC
s = list(input())
t = list(input())

s = sorted(s,reverse = False)
t = sorted(t,reverse = True)

s = ''.join(s)
t = ''.join(t)
if s < t:
    print('Yes')
else:
    print('No')
