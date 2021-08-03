from sys import stdin
from heapq import heapify
inFile = stdin
tokens = []
tokens_next = 0


def next_str():
    nonlocal tokens, tokens_next
    while tokens_next >= len(tokens):
        tokens = inFile.readline().split()
        tokens_next = 0
    tokens_next += 1
    return tokens[tokens_next - 1]


def nextInt():
    return int(next_str())


def score(a, d):
    low = -1
    high = len(a)
    while low + 1 < high:
        mid = (low + high) // 2
        if a[mid] <= d:
            low = mid
        else:
            high = mid
    return (low + 1) * 2 + (len(a) - (low + 1)) * 3


def diff(a, b, d):
    return score(a, d) - score(b, d)


n = nextInt()
a = [nextInt() for i in range(n)]
n = nextInt()
b = [nextInt() for i in range(n)]

a.sort()
b.sort()

best_dis = 0
best_score = diff(a, b, best_dis)

for d in a + b:
    cur = diff(a, b, d)
    if cur > best_score:
        best_dis = d
        best_score = cur
    elif cur == best_score:
        if score(a, d) > score(a, best_dis):
            best_dis = d
            best_score = cur

# print score(a, best_dis), ':', score(b, best_dis)
print('%d:%d' % (score(a, best_dis), score(b, best_dis)))
