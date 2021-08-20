import re


def count(s):
    return len(re.findall('VK', s))


s = input().strip()
best = count(s)
for i in range(len(s)):
    cur_s = s[:i] + 'V' + s[i + 1:]
    best = max(best, count(cur_s))
    cur_s = s[:i] + 'K' + s[i + 1:]
    best = max(best, count(cur_s))
print(best)
