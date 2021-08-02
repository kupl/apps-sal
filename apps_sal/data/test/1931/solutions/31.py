import bisect
seq = [i * (3 * i + 1) // 2 for i in range(30000)]


def solve():
    n = int(input())
    cnt = 0
    while n > 1:
        p = bisect.bisect_left(seq, n + 1) - 1
        n -= seq[p]
        cnt += 1
    return cnt


tests = int(input())
for _ in range(tests):
    print(solve())
