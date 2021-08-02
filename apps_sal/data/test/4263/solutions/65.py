S = input()
cnt = 0
res = 0
for s in S:
    if s in "AGCT":
        cnt += 1
        res = max(res, cnt)
    else:
        cnt = 0
print(res)
