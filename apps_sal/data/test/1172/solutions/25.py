from itertools import accumulate
import sys
input = sys.stdin.readline
MOD = 10 ** 9 + 7
S = input()
n = len(S)
acc_A = [0] * n
acc_C = [0] * n
acc_Q_left = [0] * n
acc_Q_right = [0] * n
cnt = 0
for (i, s) in enumerate(S):
    if s == 'A':
        acc_A[i] = 1
    elif s == 'C':
        acc_C[i] = 1
    elif s == '?':
        acc_Q_left[i] = 1
        acc_Q_right[i] = 1
        cnt += 1
acc_A = list(accumulate(acc_A))
acc_C = list(accumulate(acc_C[::-1]))[::-1]
acc_Q_left = list(accumulate(acc_Q_left))
acc_Q_right = list(accumulate(acc_Q_right[::-1]))[::-1]
ans = 0
for (i, s) in enumerate(S):
    if i == 0 or i == n - 1:
        continue
    if s == 'B':
        ans += acc_A[i - 1] * acc_C[i + 1] * pow(3, cnt, MOD)
        if cnt >= 1:
            ans += acc_A[i - 1] * acc_Q_right[i + 1] * pow(3, cnt - 1, MOD)
            ans += acc_Q_left[i - 1] * acc_C[i + 1] * pow(3, cnt - 1, MOD)
        if cnt >= 2:
            ans += acc_Q_left[i - 1] * acc_Q_right[i + 1] * pow(3, cnt - 2, MOD)
    elif s == '?':
        ans += acc_A[i - 1] * acc_C[i + 1] * pow(3, cnt - 1, MOD)
        if cnt >= 2:
            ans += acc_A[i - 1] * acc_Q_right[i + 1] * pow(3, cnt - 2, MOD)
            ans += acc_Q_left[i - 1] * acc_C[i + 1] * pow(3, cnt - 2, MOD)
        if cnt >= 3:
            ans += acc_Q_left[i - 1] * acc_Q_right[i + 1] * pow(3, cnt - 3, MOD)
    ans %= MOD
print(ans)
