from collections import Counter

def read_line():
    return list(map(int, input().split()))


n = int(input())
l = sorted(read_line())
def ok(ans):
    nums = l[:ans]
    rest = l[ans:]
    if len(rest) < ans + 1:
        return None
    rest = rest[-(ans + 1):]
    l2 = []
    for i in range(len(nums)):
        if nums[i] < rest[i] and nums[i] < rest[i+1]:
            l2.append(rest[i])
            l2.append(nums[i])
        else:
            return None
    l2.append(rest[-1])
    r = Counter(l)
    s = Counter(l2)
    for v in r:
        k = r[v] - s[v]
        l2 += [v] * k
    return l2

def _ok(ans):
    nums = l[:ans]
    rest = l[ans:]
    if len(rest) < ans + 1:
        return None
    rest = rest[-(ans + 1):]
    for i in range(len(nums)):
        if nums[i] < rest[i] and nums[i] < rest[i+1]:
            pass
        else:
            return None
    return 1


lo = 0
hi = n
while lo <= hi:
    mid = (lo + hi) // 2
    if _ok(mid) is not None:
        lo = mid + 1
    else:
        hi = mid - 1
a = ok(hi)
print(hi)
print(" ".join(map(str, a)))

