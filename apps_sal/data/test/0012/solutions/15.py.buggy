import sys
from math import ceil, sqrt

input = sys.stdin.readline

n = int(input())
s = input().strip()

last = "S"
ans = []
count = 0
freq = {'S': 0, 'G': 0}

for i in range(n):
    freq[s[i]] += 1
    if s[i] != last:
        ans.append((count, last))
        last = s[i]
        count = 1
    else:
        count += 1
ans.append((count, last))
ans.pop(0)

if freq['G'] == 0:
    print(0)
    return

final = max([x[0] for x in ans if x[1] == 'G'])
if freq['G'] > final:
    final += 1

for i in range(len(ans) - 2):
    if ans[i][1] == 'G' and ans[i + 1][1] == 'S' and ans[i + 1][0] == 1 and ans[i + 2][1] == 'G':
        if freq['G'] > ans[i][0] + ans[i + 2][0]:
            final = max(final, ans[i][0] + ans[i + 2][0] + 1)
        else:
            final = max(final, ans[i][0] + ans[i + 2][0])
print(final)
