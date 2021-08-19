S = list(input())
T = list(input())
count = len(S)
ans = 0
for i in range(count):
    if S[i] != T[i]:
        ans += 1
    else:
        pass
print(ans)
