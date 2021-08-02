s = input()
t = input()
ln = len(s)
cnt = 0
for i in range(ln):
    if s[i] != t[i]:
        cnt += 1
print(cnt)
