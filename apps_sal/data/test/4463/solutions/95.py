s = input()
t = input()
ord_s = []
ord_t = []

for i in range(len(s)):
    ord_s.append(ord(s[i]))
else:
    ord_s.sort()

for i in range(len(t)):
    ord_t.append(ord(t[i]))
else:
    ord_t.sort(reverse=True)

for i in range(min(len(s), len(t))):
    if ord_s[i] < ord_t[i]:
        print('Yes')
        break
    elif ord_s[i] == ord_t[i]:
        pass
    else:
        print('No')
        break
else:
    if len(s) < len(t):
        print('Yes')
    else:
        print('No')
