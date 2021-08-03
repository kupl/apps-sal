S = input()

L = {}

ans = "Yes"
for s in S:
    if s in list(L.keys()):
        L[s] += 1
        if L[s] > 2:
            ans = "No"
    else:
        L[s] = 1
if len(list(L.keys())) != 2:
    ans = "No"

print(ans)
