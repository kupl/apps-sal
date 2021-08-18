s = input()
t = input()
if t in s:
    print(0)
    return
ns = len(s)
nt = len(t)
ans = nt
k = ns - nt
for i in range(k + 1):
    hoge = s[i:i + nt]
    c = 0
    for j in range(nt):
        if hoge[j] != t[j]:
            c += 1
    ans = min(c, ans)
print(ans)
