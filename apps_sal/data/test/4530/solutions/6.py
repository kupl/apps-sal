from collections import Counter
import sys
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__


def go():
    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    m = len(c)
    best = -1
    for cnt in list(c.values()):
        best = max(best, min(cnt, m - 1))
        best = max(best, min(cnt - 1, m))
    return best


t = int(input())
ans = []
for _ in range(t):
    ans.append(str(go()))
print('\n'.join(ans))
