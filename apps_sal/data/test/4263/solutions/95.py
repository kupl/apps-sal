S = input()
ans = 0
for i in range(len(S)):
    cnt = 0
    for j in range(i, len(S)):
        if S[j] in ['A', 'C', 'G', 'T']:
            cnt += 1
        else:
            break
    ans = max(ans, cnt)
print(ans)
