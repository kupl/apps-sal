from collections import Counter

s = input()

c = Counter(s)

if c['o'] == 0:
    print("YES")
else:
    print("YES" if c['-'] % c['o'] == 0 else "NO")
