

S = input()

cnt = 0
ans = 0

for i in range(len(S)):
    if S[i] == 'R':
        cnt = cnt + 1
        if ans < cnt:
            ans = cnt
    else:
        cnt = 0

print(ans)
