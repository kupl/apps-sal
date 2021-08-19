from bisect import bisect_right
s = input()
t = input()
alpha = [[] for _ in range(26)]


def f(c):
    return ord(c) - ord('a')


for (i, c) in enumerate(s):
    alpha[f(c)].append(i)
idx = -1
loop = 0
for c in t:
    lst = alpha[f(c)]
    if not lst:
        ans = -1
        break
    i = bisect_right(lst, idx)
    if i == len(lst):
        loop += 1
        idx = lst[0]
    else:
        idx = lst[i]
else:
    ans = len(s) * loop + idx + 1
print(ans)
