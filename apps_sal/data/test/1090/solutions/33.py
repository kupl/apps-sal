N, K = list(map(int, input().split()))
S = input()
if N == 1:
    print((0))
    return
if N == 2:
    if K >= 1:
        print((1))
    else:
        print((0))
        return


ans = 0
d = 0
for i, s in enumerate(S[:-1]):
    if S[i] == S[i + 1]:
        ans += 1
# print(ans)
ans += 2 * K
print((min(ans, N - 1)))
