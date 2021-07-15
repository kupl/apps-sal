s = input()
tmp = s[0]
cnt = 0
for c in s:
    if tmp != c:
        tmp = c
        cnt += 1
print(cnt)
