n = int(input())
s = input()
cnt_e = [0] * n
cnt_w = [0] * n
for i in range(n):
    if i == 0:
        if s[i] == 'E':
            cnt_e[i] = 1
        else:
            cnt_w[i] = 1
    elif s[i] == 'E':
        cnt_e[i] = cnt_e[i - 1] + 1
        cnt_w[i] = cnt_w[i - 1]
    else:
        cnt_e[i] = cnt_e[i - 1]
        cnt_w[i] = cnt_w[i - 1] + 1
ans = 3 * 10 ** 5 + 1
for i in range(n):
    if s[i] == 'E':
        e = cnt_e[-1] - cnt_e[i]
        w = cnt_w[i]
    else:
        e = cnt_e[-1] - cnt_e[i]
        w = cnt_w[i] - 1
    ans = min(ans, e + w)
print(ans)
