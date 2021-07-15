from collections import Counter
S = list(input())
S = Counter(S)
for i in list(S.values()):
    if i == 2 and len(S) == 2:
        ans = "Yes"
    else:
        ans = "No"
    break
print(ans)

