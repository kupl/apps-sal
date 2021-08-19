(N, K) = list(map(int, input().split()))
(R, S, P) = list(map(int, input().split()))
T = input()
ans = [''] * N
point = 0
for (i, t) in enumerate(T):
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
