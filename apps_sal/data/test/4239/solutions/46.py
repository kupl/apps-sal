import sys

N = int(sys.stdin.readline())
s_max = N // 6
n_max = N // 9

s_n = 6
s_c = 0
while s_n < N:
    s_n *= 6
    s_c += 1

n_n = 9
n_c = 0
while n_n < N:
    n_n *= 9
    n_c += 1

ans = float("inf")
for i in range(s_max + 1):
    j = (N - 6 * i) // 9
    o = N - 6 * i - 9 * j
    if o < 0:
        continue
    tmp_ans = o + i + j
    ans = min(ans, tmp_ans)
    tmp = 6 ** s_c
    while 0 < tmp:
        r = i // tmp
        i -= r * tmp
        tmp_ans += r - r * tmp
        tmp //= 6

    tmp = 9 ** n_c
    while 0 < tmp:
        r = j // tmp
        j -= r * tmp
        tmp_ans += r - r * tmp
        tmp //= 9

    ans = min(ans, tmp_ans)

print(ans)
