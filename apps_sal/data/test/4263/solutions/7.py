import re
s = input()
res = re.findall(r'[ATGC]+', s)
ans = 0

for e in res:
    ans = max(ans, len(e))

print(ans)
