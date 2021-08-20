import math
(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))


def calc_ans(k, a, b):
    div = (10 ** k - 1) // a + 1
    b_min = b * 10 ** (k - 1)
    b_max = (b + 1) * 10 ** (k - 1) - 1
    d_min_inc = math.ceil(b_min / a)
    d_max_inc = math.floor(b_max / a)
    return div - (d_max_inc - d_min_inc + 1)


p = 10 ** 9 + 7
ans = 1
for (ai, bi) in zip(a, b):
    ans = ans * calc_ans(k, ai, bi) % p
print(ans)


def easy_calc(k, a, b):
    ans = 0
    for i in range(10 ** k):
        c = str(i)
        first = int(c[0]) if len(c) == k else 0
        if i % a == 0 and (not first == b):
            ans += 1
    return ans
