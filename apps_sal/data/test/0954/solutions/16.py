s = input()
n = len(s)
s += s
dl = len(s)
d = set()
ans = 0
for i in range(dl - n):
    str = s[i:i + n]
    if not str in d:
        ans += 1
        d.add(str)
print(ans)
