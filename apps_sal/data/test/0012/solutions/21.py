def longestSubSeg(a, n):
    cnt0 = 0
    l = 0
    max_len = 0
    ctG = 0
    for i in range(0, n):
        if a[i] == 'S':
            cnt0 += 1
        if a[i] == 'G':
            ctG += 1
        while (cnt0 > 1):
            if a[l] == 'S':
                cnt0 -= 1
            l += 1

        max_len = max(max_len, i - l + 1)
    if max_len > ctG:
        return max_len - 1
    return max_len


n = int(input())
a = list(input())
print(longestSubSeg(a, n))
