import sys
input = sys.stdin.readline


def make_divisors(n):
    """自然数nの約数を列挙したリストを出力する
    計算量: O(sqrt(N))
    入出力例: 12 -> [1, 2, 3, 4, 6, 12]
    """
    divisors = []
    for k in range(1, int(n**0.5) + 1):
        if n % k == 0:
            divisors.append(k)
            if k != n // k:
                divisors.append(n // k)
    divisors = sorted(divisors)
    return divisors


div_list = [None] * (10**4 + 30)
for i in range(1, 10**4 + 30):
    div_list[i] = make_divisors(i)

t = int(input())
INF = 10**6
for _ in range(t):
    ans_a = -1
    ans_b = -1
    ans_c = -1
    ans = INF
    a, b, c = list(map(int, input().split()))
    for tmp_b in range(1, 10**4 + 30):
        cost_b = abs(b - tmp_b)

        cost_a = INF
        for tmp_a in div_list[tmp_b]:
            if cost_a > abs(a - tmp_a):
                cost_a = abs(a - tmp_a)
                aa = tmp_a

        cost_c = INF
        num = c // tmp_b
        cost_c = INF
        if cost_c > abs(c - num * tmp_b):
            cost_c = abs(c - num * tmp_b)
            cc = num * tmp_b
        if cost_c > abs(c - (num + 1) * tmp_b):
            cost_c = abs(c - (num + 1) * tmp_b)
            cc = (num + 1) * tmp_b
        if cost_c > abs(c - (num - 1) * tmp_b):
            cost_c = abs(c - (num - 1) * tmp_b)
            cc = (num - 1) * tmp_b
        tmp_ans = cost_a + cost_b + cost_c
        if ans > tmp_ans:
            ans = tmp_ans
            ans_b = tmp_b
            ans_a = aa
            ans_c = cc
    print(ans)
    print(ans_a, ans_b, ans_c)
