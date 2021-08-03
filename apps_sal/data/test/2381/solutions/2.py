import sys

input = sys.stdin.readline

n_k = list(map(int, input().split()))
n = n_k[0]
k = n_k[1]
a = list(map(int, input().split()))
a_pos = list([v for v in a if v >= 0])
a_neg = list([v for v in a if v < 0])

a_pos.sort(reverse=True)
a_neg.sort()

mod = 10**9 + 7

ans = 1
if n == k:
    for a_i in a:
        ans = ans * a_i % mod
elif len(a_pos) == 0 and k % 2 == 1:
    for i in reversed(list(range(len(a_neg) - k, len(a_neg)))):
        ans = ans * a_neg[i] % mod
else:
    i_p = 0
    i_n = 0
    i = 0
    while i < k:
        if i_p < len(a_pos) and (i == k - 1 or i_n + 1 >= len(a_neg) or a_pos[i_p] * (a_pos[i_p + 1] if i_p + 1 < len(a_pos) else 1) > a_neg[i_n] * a_neg[i_n + 1]):
            ans = ans * a_pos[i_p] % mod
            i_p += 1
            i += 1
        else:
            ans = ans * a_neg[i_n] % mod * a_neg[i_n + 1] % mod
            i_n += 2
            i += 2
print(ans)
