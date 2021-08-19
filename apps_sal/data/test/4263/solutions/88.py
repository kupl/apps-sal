S = input()
ans = 0
cnt = 0
for i in list(S):
    if i in ('A', 'T', 'C', 'G'):
        cnt += 1
        ans = max(ans, cnt)
    else:
        cnt = 0
print(ans)
