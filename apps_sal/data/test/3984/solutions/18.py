from collections import Counter
import sys
input = sys.stdin.readline


s = input().strip('\n')
c = Counter(s)
l = sorted(list(c))
ans = []
# print(s)
mi = [1] * (len(s))
curr = s[0]
for i in range(1, len(s)):
    if curr < s[i]:
        mi[i] = 0
    curr = min(curr, s[i])


for i in range(len(s)):
    # print(i)
    if i == 0 or mi[i]:
        ans.append('Mike')
    else:
        ans.append('Ann')
for i in ans:
    print(i)
