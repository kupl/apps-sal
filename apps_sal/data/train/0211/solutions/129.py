def count1(x):
    xx = x
    ans = 0
    while x != 0:
        x &= x - 1
        ans += 1
    return ans

def ok(mask, s):
    strs = []
    prev = 0
    for i in range(len(s) - 1):
        if (1 << i) & mask:
            strs.append(s[prev: i+1])
            prev = i + 1
    strs.append(s[prev:])
    # print(strs)
    return len(set(strs)) == len(strs)

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(1, 1 << (n-1)):
            if ok(i, s):
                ans = max(count1(i), ans)
        return ans + 1
