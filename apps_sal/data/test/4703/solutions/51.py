S = input()
ans = 0

for i in range(0, 2**(len(S) - 1)):
    tmp = S
    cnt = 0
    for j in range(0, len(S)):
        if (i >> j) & 1:
            cnt += 1
            tmp = tmp[0:j + cnt] + '+' + tmp[j + cnt:]
    ans += eval(tmp)
print(ans)
