arr = [1, 1]
M = 10 ** 9 + 7
for i in range(10**5):
    arr.append((arr[-1] + arr[-2]) % M)


def f(symb):
    nonlocal s, arr
    local_ans = 1
    if s[0] == symb:
        cnt = 1
    else:
        cnt = 0
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            if cnt > 0:
                local_ans *= arr[cnt]
                local_ans %= M
            if cnt == 0 and s[i] == symb:
                cnt = 1
            if s[i] != symb:
                cnt = 0
        if s[i] == s[i - 1] and s[i] == symb:
            cnt += 1
    if cnt > 0:
        local_ans *= arr[cnt]
        local_ans %= M
    # print(local_ans)
    return local_ans


ans = 1
s = input()
if s.count('w') or s.count('m'):
    print(0)
else:
    print(f('u') * f('n') % M)
