n, k = [int(x) for x in input().split()]
lr = [[int(x) for x in input().split()] for _ in range(k)]

accsum = [0, 1] + [0] * n


def sum_between(l: int, r: int) -> int:
    if r >= 1:
        return accsum[r] - accsum[max(l - 1, 0)]
    else:
        return 0


for i in range(2, n + 1):
    accsum[i] = (accsum[i - 1] + sum(sum_between(i - r, i - l) for l, r in lr)) \
        % 998244353


print(((accsum[n] - accsum[n - 1]) % 998244353))
