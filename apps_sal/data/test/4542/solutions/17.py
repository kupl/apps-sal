S = input()
cnt = 0
now = S[0]
for i in S:
    if i != now:
        now = i
        cnt += 1
print(cnt)
