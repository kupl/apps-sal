S = input()
N = len(S)
ans = [0] * N
lr_idx = 0
for i in range(N - 1):
    if S[i] == 'R' and S[i + 1] == 'L':
        r_odd = 0
        r_even = 0
        for (c, j) in enumerate(reversed(list(range(lr_idx, i)))):
            if S[j] == 'R':
                if (c + 1) % 2 == 0:
                    r_even += 1
                else:
                    r_odd += 1
        l_odd = 0
        l_even = 0
        for (c, j) in enumerate(range(i + 2, N)):
            if S[j] == 'R' and S[j + 1] == 'L':
                break
            if S[j] == 'L':
                if (c + 1) % 2 == 0:
                    l_even += 1
                else:
                    l_odd += 1
        ans[i] = 1 + r_even + l_odd
        ans[i + 1] = 1 + r_odd + l_even
        lr_idx = i + 2
print(' '.join(map(str, ans)))
