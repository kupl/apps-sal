n = int(input())
strs = []
for i in range(n):
    strs.append(input())


def check(s):
    h = 0
    min_h = max_h = 0
    s = s.strip()
    for c in s:
        if c == '(':
            h += 1
        elif c == ')':
            h -= 1
        else:
            raise NotImplementedError()
        min_h = min(h, min_h)
        max_h = max(h, max_h)
    if min(0, h) == min_h:
        return h
    else:
        return None


def count_pairs(strs):
    by_height = {}
    for s in strs:
        h = check(s)
        if h not in by_height:
            by_height[h] = 0
        by_height[h] += 1
    pairs_count = 0
    for (h, c) in list(by_height.items()):
        if h is not None and h > 0:
            pairs_count += min(by_height[h], by_height.get(-h, 0))
    pairs_count += by_height.get(0, 0) // 2
    return pairs_count


print(count_pairs(strs))
