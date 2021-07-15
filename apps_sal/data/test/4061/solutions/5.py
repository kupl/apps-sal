s = input()
t = input()


def compute_prefix(s, t):
    prefix = [0 for i in range(len(t) + 1)]
    i = 0
    j = 0
    while i < len(t):
        while s[j] != t[i]:
            j += 1
        prefix[i+1] = j+1
        i += 1
        j += 1
    return prefix


prefix = compute_prefix(s, t)
suffix = compute_prefix(s[::-1], t[::-1])
res = 0
for i in range(len(t) + 1):
    res = max(res, len(s) - (prefix[i] + suffix[len(t) - i]))
print(res)

