from operator import itemgetter


def solve(n, ppp):
    qqq = sorted(enumerate(ppp), key=itemgetter(1))
    left_next_index = list(range(-1, n - 1)) + [-1, -1]
    right_next_index = list(range(1, n + 1)) + [n, n]
    ans = 0
    for (i, p) in qqq:
        l2 = left_next_index[i]
        l1 = left_next_index[l2]
        r1 = right_next_index[i]
        r2 = right_next_index[r1]
        ans += p * ((l2 - l1) * (r1 - i) + (r2 - r1) * (i - l2))
        left_next_index[r1] = l2
        right_next_index[l2] = r1
    return ans


n = int(input())
ppp = list(map(int, input().split()))
print(solve(n, ppp))
