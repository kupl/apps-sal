N, K = list(map(int, input().split()))
R, S, P = list(map(int, input().split()))
T = input()

# point = {'r':P, 's':R, 'p':S}
# skip = {'r':[], 's':[], 'p':[]}

# ans = 0
# cnt = 0
# for i in range(N):
# 	cnt += 1
# 	spell = T[i]
# 	if i < K:
# 		ans += point[spell]
# 		continue
# 	if T[i - K] == spell:
# 		if i - K in skip[spell]:
# 			ans += point[spell]
# 		else:
# 			skip[spell].extend([i])
# 	else:
# 		ans += point[spell]
# print(ans)

ans = [''] * N
point = 0

for i, t in enumerate(T):
    if t == 'r':
        ans_tmp = 'p'
        point_tmp = P
    elif t == 's':
        ans_tmp = 'r'
        point_tmp = R
    elif t == 'p':
        ans_tmp = 's'
        point_tmp = S

    if i - K >= 0:
        if ans[i - K] == ans_tmp:
            ans_tmp = ''
            point_tmp = 0

    ans[i] = ans_tmp
    point += point_tmp

print(point)
