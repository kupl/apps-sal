S = input()

res = 0
cnt = 0
for i in range(len(S)):
    if S[i] in ['A', 'T', 'G', 'C']:
        cnt += 1
    else:
        res = max(res, cnt)
        cnt = 0

res = max(res, cnt)

print(res)
