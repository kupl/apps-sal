from collections import defaultdict
s = input()
t = input()
n = len(s)

d = defaultdict(str)
# ダメな場合
# 1. 同じtが違うsに対応
# 2. 同じsが違うtに対応
for i in range(n):
    if d[t[i]] == "":
        d[t[i]] = s[i]
    elif d[t[i]] != s[i]:
        print("No")
        return
d.clear()
for i in range(n):
    if d[s[i]] == "":
        d[s[i]] = t[i]
    elif d[s[i]] != t[i]:
        print("No")
        return

print("Yes")
