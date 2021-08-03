N = int(input())
S = input()

oS = S
S = list(S)

cnt = 0
while True:
    p_cnt = cnt
    for i in range(len(S) - 1):
        if S[i] == "(" and S[i + 1] == ")":
            S.pop(i + 1)
            S.pop(i)
            cnt += 1
            break

    if cnt == p_cnt:
        break

cnt_open = 0
cnt_close = 0

for s in S:
    if s == "(":
        cnt_open += 1
    else:
        cnt_close += 1

ans = ("(" * cnt_close) + oS + (")" * cnt_open)
print(ans)
