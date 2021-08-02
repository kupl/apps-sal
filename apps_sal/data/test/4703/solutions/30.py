s = input()
n = len(s) - 1
ans = 0
for i in range(2**n):
    op = [0] * n
    for j in range(n):
        if ((i >> j) & 1):
            op[j] = 1
    t = s[0]
    for j in range(1, n + 1):
        if op[j - 1] == 1:
            t += '+' + s[j:j + 1]
        else:
            t += s[j:j + 1]
    ans += sum(list(map(int, t.split('+'))))
print(ans)
