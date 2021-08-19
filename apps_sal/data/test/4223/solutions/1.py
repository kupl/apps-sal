N = int(input())
S = list(input())
ans = []
while len(S) > 1:
    if S[0] == S[1]:
        S.pop(0)
    else:
        ans.append(S.pop(0))
print(len(ans) + 1)
