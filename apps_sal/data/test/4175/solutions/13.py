import collections
N = int(input())
W = []
f = input()
W.append(f)
ans = "Yes"
for _ in range(N - 1):
    w = input()
    if f[-1] != w[0]:
        ans = "No"
    W.append(w)
    f = w

cnt = collections.Counter(W)
for v in cnt.values():
    if v >= 2:
        ans = "No"

print(ans)
