from itertools import accumulate
n, m = map(int, input().split())
a = list(map(int, input().split()))
ls_0 = [0 for i in range(m * 2 + 2)]
ans_0 = 0
for i in range(1, n):
    if a[i - 1] < a[i]:
        l = a[i - 1] + 2
        r = a[i] + 1
    else:
        l = a[i - 1] + 2
        r = a[i] + m + 1
    ls_0[l] += 1
    ls_0[r] -= (r - l + 1)
    ls_0[r + 1] += r - l
    ans_0 += r - l + 1

ls_1 = list(accumulate(ls_0))
ls_2 = list(accumulate(ls_1))
ls_3 = [0] + [ls_2[i] + ls_2[i + m] for i in range(1, m + 1)]
print(ans_0 - max(ls_3))
