N, P = map(int, input().split())
S = str(input())
L = len(S)
ans = 0
dic = {0: 1}  # 一番右端は0なのでこれは常に必要
now = 0
if P == 2 or P == 5:
    kotae = 0
    for i in range(L):
        if int(S[L - 1 - i]) % P == 0:
            kotae += L - i
    print(kotae)
    return
else:
    for i in range(L):
        now += int(S[L - 1 - i]) * pow(10, i, P)
        temp = now % P
        if temp not in dic:
            dic[temp] = 1
        else:
            dic[temp] += 1
# print(dic)
ans = 0
for i in dic.values():
    if i != 1:
        ans += i * (i - 1) // 2
print(ans)
