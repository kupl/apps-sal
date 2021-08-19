from operator import itemgetter
from sys import stdin, stdout


def solve(a, k):
    aa = list(map(lambda x: [x[1], x[0]], enumerate(a)))
    aa.sort(reverse=True, key=itemgetter(0))
    if aa[0][0] < 0:
        return aa[0][0]
    best = -float('inf')
    for i in range(len(a)):
        for j in range(1, len(a) + 1):
            in_range = sorted(a[i:j], reverse=True)
            out_of_range = sorted(a[:i] + a[j:])
            additional = []
            for kk in range(k):
                if len(out_of_range) > 0 and len(in_range) > 0 and (in_range[-1] < out_of_range[-1]):
                    in_range.pop()
                    additional.append(out_of_range.pop())
            best = max(best, sum(in_range + additional))
    return best


def __starting_point():
    (n, k) = map(int, stdin.readline().split())
    a = [int(x) for x in stdin.readline().split()]
    stdout.write('{}\n'.format(solve(a, k)))


__starting_point()
