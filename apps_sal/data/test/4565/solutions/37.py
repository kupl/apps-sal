N = int(input())
S = input()


w_cnt = 0
e_cnt = 0
w_lst = []
e_lst = []

for s in S:
    if s == 'W':
        w_cnt += 1

    else:
        e_cnt += 1

    w_lst.append(w_cnt)
    e_lst.append(e_cnt)

ans = float('inf')
e_all = e_lst[-1]
for i in range(N):
    if S[i] == 'W':
        t = w_lst[i] - 1 + e_all - e_lst[i]
    else:
        t = w_lst[i] + e_all - e_lst[i]

    ans = min(ans, t)


print(ans)
