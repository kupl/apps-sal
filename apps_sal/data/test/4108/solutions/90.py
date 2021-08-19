from collections import Counter
S = list(input())
T = list(input())
change = [-1] * 27
ans = 'Yes'
for i in range(len(S)):
    s = ord(S[i]) - 97
    if S[i] == T[i]:
        change[s] = s
    elif change[s] == -1:
        change[s] = ord(T[i]) - 97
    else:
        t = ord(T[i]) - 97
        if change[s] != t:
            ans = 'No'
            break
change = Counter(change)
del change[-1]
for i in change.values():
    if i == 1:
        continue
    else:
        ans = 'No'
print(ans)
