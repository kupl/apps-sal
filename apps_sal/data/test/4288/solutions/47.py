(A, B, C) = input().split()
S = A + B + C
ans = 'No'
for i in range(len(S)):
    if S.count(S[i]) == 2:
        ans = 'Yes'
        break
print(ans)
