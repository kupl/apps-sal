s = list(input())
t = list(input())

s.sort()
t.sort(reverse=True)

for i in range(min(len(s), len(t))):
    if s[i] < t[i]:
        print('Yes')
        break
    elif s[i] > t[i]:
        print('No')
        break
    else:
        continue
else:
    if len(t) > len(s):
        print('Yes')
    else:
        print('No')
