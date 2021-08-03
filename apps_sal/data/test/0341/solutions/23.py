from collections import deque


def calc(t, r, s, p):
    if t == "r":
        return p
    elif t == "s":
        return r
    else:
        return s


n, k = list(map(int, input().split()))
r, s, p = list(map(int, input().split()))
T = input()
d = deque()
ans = 0
for i, t in enumerate(T):
    if i < k:
        ans += calc(t, r, s, p)
        d.append(t)
    else:
        x = d.popleft()
        if x == t:
            d.append(0)
        else:
            ans += calc(t, r, s, p)
            d.append(t)
print(ans)
