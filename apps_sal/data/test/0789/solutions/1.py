n = (input())
s = []
for i in range(len(n) - 1, -1, -1):
    if int(n[i]) == 4:
        s.append(1)
    else:
        s.append(2)
cnt = 0
for i in range(len(s)):
    cnt += (2**i) * s[i]
print(cnt)
