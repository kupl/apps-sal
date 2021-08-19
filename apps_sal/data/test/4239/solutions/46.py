import sys

N = int(sys.stdin.readline())
s_max = N // 6
n_max = N // 9

s_n = 6
s_c = 0
while s_n < N:
    s_n *= 6
    s_c += 1
# print(6**s_c)

n_n = 9
n_c = 0
while n_n < N:
    n_n *= 9
    n_c += 1
# print(9**n_c)

ans = float("inf")
for i in range(s_max + 1):
    # print("#####", i, "#####")
    j = (N - 6 * i) // 9
    o = N - 6 * i - 9 * j
    if o < 0:
        continue
    tmp_ans = o + i + j
    ans = min(ans, tmp_ans)
    # i, jをx乗で差し替えて最小の操作回数を求める
    tmp = 6 ** s_c
    while 0 < tmp:
        r = i // tmp
        i -= r * tmp
        # print("i", i)
        tmp_ans += r - r * tmp
        tmp //= 6

    tmp = 9 ** n_c
    while 0 < tmp:
        r = j // tmp
        j -= r * tmp
        # print("j", j)
        tmp_ans += r - r * tmp
        tmp //= 9

    # print(tmp_ans)
    ans = min(ans, tmp_ans)

print(ans)
