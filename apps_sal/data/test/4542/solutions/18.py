S = input()
prev = S[0]
cnt = 0
for s in S:
    if prev != s:
        cnt += 1
    prev = s
print(cnt)
