S = str(input())
ans = 0
for i in range(len(S)):
    for j in range(len(S)):
        cnt = 0
        flag = True
        for k in S[i:j + 1]:
            if k == 'A' or k == 'C' or k == 'G' or (k == 'T'):
                cnt += 1
            else:
                flag = False
        if flag:
            ans = max(ans, cnt)
print(ans)
