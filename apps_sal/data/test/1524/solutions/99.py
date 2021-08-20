s = input()
ans = [0] * len(s)
s += 'R'
present = 'R'
start = 0
for i in range(len(s) - 1):
    if present == 'R':
        if s[i + 1] == 'R':
            continue
        r = i
        l = i + 1
        present = 'L'
    else:
        if s[i + 1] == 'L':
            continue
        end = i
        present = 'R'
        rl = r - start
        ll = end - l
        ans[r] = 1 + rl // 2 + -(-ll // 2)
        ans[l] = 1 + -(-rl // 2) + ll // 2
        start = i + 1
print(' '.join(map(str, ans)))
