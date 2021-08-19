from collections import Counter
S = input()
c = Counter(S)
ans = 'No'
if len(c) == 2:
    if all([x for x in c.values() if x == 2]):
        ans = 'Yes'
print(ans)
