N, M = list(map(int, input().split()))
a_s = set([int(input()) for _ in range(M)])

mod = 10 ** 9 + 7
ans = [0] * (N + 1)
ans[0] = 1

for i in range(1, N + 1):
    if i - 1 not in a_s:
        ans[i] = ans[i - 1]
    if i > 1:
        if i - 2 not in a_s:
            ans[i] += ans[i - 2]
    if i - 1 in a_s and i - 2 in a_s:
        break
    else:
        ans[i] = ans[i] % mod

print((ans[-1]))
