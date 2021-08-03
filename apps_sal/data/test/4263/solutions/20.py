# B - ATCoder
S = list(input())

ans = 0
for i in range(len(S)):
    for j in range(i, len(S) + 1):
        tgt = S[i:j]
        cnt = 0
        for s in tgt:
            if s == 'A' or s == 'C' or s == 'G' or s == 'T':
                cnt += 1
            else:
                cnt = 0
                break
        ans = max(cnt, ans)
print(ans)
