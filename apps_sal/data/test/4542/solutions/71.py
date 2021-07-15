S = input()
now = S[0]
cnt = 0
for s in S:
    if now == s:
        continue
    cnt += 1
    now = s
print(cnt)
