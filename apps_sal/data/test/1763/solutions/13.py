
import bisect
N, A, R, M = list(map(int, input().split()))

aa = sorted(map(int, input().split()))

raa = [0]
for a in aa:
    raa.append(raa[-1] + a)

ans = 10 ** 15


def calc(a):
    i = bisect.bisect_right(aa, a)
    add_n = a * i - raa[i]
    rem_n = (raa[-1] - raa[i]) - (a * (N - i))

    if rem_n < add_n:
        tmp1 = rem_n * M + (add_n - rem_n) * A
    else:
        tmp1 = add_n * M + (rem_n - add_n) * R

    tmp2 = rem_n * R + add_n * A

    return min(tmp1, tmp2)


ans = min([calc(a) for a in set(aa)])

tmp = sum(aa) // N

ans = min([ans, calc(tmp), calc(tmp + 1)])


print(ans)
