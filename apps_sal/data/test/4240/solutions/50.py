S = list(input())
T = list(input())
ans = 'No'
for i in S:
    tmp = S.pop()
    S.insert(0, tmp)
    ''.join(S)
    if S == T:
        ans = 'Yes'
        break
print(ans)
