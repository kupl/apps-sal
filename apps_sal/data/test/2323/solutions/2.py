from collections import defaultdict as dd
import math


def nn():
    return int(input())


def li():
    return list(input())


def mi():
    return list(map(int, input().split()))


def lm():
    return list(map(int, input().split()))


n = nn()
strings = lm()
q = nn()
strings.sort()
diffs = []
for i in range(1, n):
    diffs.append(strings[i] - strings[i - 1])
diffs.sort(reverse=True)
if not n == 1:
    runninggaps = [diffs[0]]
for i in range(1, n - 1):
    runninggaps.append(runninggaps[-1] + diffs[i])
answers = []
for i in range(q):
    (l, r) = mi()
    if n == 1:
        answers.append(r - l + 1)
        continue
    gap = r - l + 1
    maxrange = strings[-1] - strings[0] + gap
    start = 0
    end = n - 2
    while start <= end:
        mid = (start + end) // 2
        if diffs[mid] > gap:
            start = mid + 1
        else:
            end = mid - 1
    if end == -1:
        pass
    else:
        maxrange += gap * (end + 1) - runninggaps[end]
    answers.append(maxrange)
print(*answers)
