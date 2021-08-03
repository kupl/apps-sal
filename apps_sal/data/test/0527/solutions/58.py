import collections

s = input()
t = input()
mod = len(s)
s_idx = dict([])
for i, key in enumerate(s):
    try:
        s_idx[key].append(i + 1)
    except KeyError:
        s_idx[key] = [i + 1]


def binary_search(li, tmp, ng, ok):
    mid = (ng + ok) // 2
    if ok - ng < 2:
        if ok == len(li):
            return mod + li[0]
        else:
            return li[ok]
    if li[mid] <= tmp:
        return binary_search(li, tmp, mid, ok)
    else:
        return binary_search(li, tmp, ng, mid)


ans = 0
tmp = 0
for key in t:
    try:
        i = binary_search(s_idx[key], tmp, -1, len(s_idx[key]))
        ans += i - tmp
        tmp = i % mod
    except KeyError:
        ans = -1
        break
print(ans)
