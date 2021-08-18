import bisect


def en2asc(s): return ord(s) - 97


S = input()
T = input()
if not set(S) >= set(T):
    print(-1)
    return

lst = [[] for _ in range(26)]
for i, s in enumerate(S):
    lst[en2asc(s)].append(i)

L = len(S)
cur = 0
for t in T:
    t = en2asc(t)
    b = bisect.bisect_left(lst[t], cur % L)
    if b == len(lst[t]):
        cur = (cur // L + 1) * L
        b = bisect.bisect_left(lst[t], cur % L)
    cur = cur // L * L + lst[t][b] + 1
print(cur)
