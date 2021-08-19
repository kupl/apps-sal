S = input()
T = input()
ans = 'Yes'
(dic1, dic2) = ({}, {})
for (i, j) in zip(S, T):
    if i in dic1:
        if dic1[i] != j:
            ans = 'No'
    else:
        dic1[i] = j
    if j in dic2:
        if dic2[j] != i:
            ans = 'No'
    else:
        dic2[j] = i
print(ans)
