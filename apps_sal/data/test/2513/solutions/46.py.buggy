n = int(input())
s = input()

# assume [0 is S, -1 is S]

for ans0, ans_last in [('S', 'S'), ('S', 'W'), ('W', 'S'), ('W', 'W')]:
    ans = ['tbd'] * n
    ans[0] = ans0
    ans[-1] = ans_last

    for i in range(n - 2):
        if (s[i] == 'o' and ans[i] == 'S') or (s[i] == 'x' and ans[i] == 'W'):
            ans[i + 1] = ans[i - 1]
        else:
            ans[i + 1] = 'S' if ans[i - 1] == 'W' else 'W'

    last_two_flag = False
    last_one_flag = False

    if (s[n - 2] == 'o' and ans[n - 2] == 'S') or (s[n - 2] == 'x' and ans[n - 2] == 'W'):
        if ans[n - 3] == ans[n - 1]:
            last_two_flag = True
    else:
        if ans[n - 3] != ans[n - 1]:
            last_two_flag = True

    if (s[n - 1] == 'o' and ans[n - 1] == 'S') or (s[n - 1] == 'x' and ans[n - 1] == 'W'):
        if ans[n - 2] == ans[0]:
            last_one_flag = True
    else:
        if ans[n - 2] != ans[0]:
            last_one_flag = True

    if last_one_flag and last_two_flag:
        print(''.join(ans))
        return

print(-1)
