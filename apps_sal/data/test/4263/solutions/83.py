s = input()
l = len(s)
cnt = 0
ans = 0

for i in range(l):
    if s[i] == 'A' or s[i] == 'C' or s[i] == 'G' or s[i] == 'T':
        cnt += 1
        if ans < cnt:
            ans = cnt
    else:
        cnt = 0

print(ans)
