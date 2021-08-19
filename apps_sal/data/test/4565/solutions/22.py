EW = 0
ans = 99999999999999999999999999999999
N = int(input())
S = input()
for i in range(N):
    if i == 0:
        pass
    elif S[i] == 'E':
        EW += 1
if ans > EW:
    ans = EW
for j in range(1, N):
    if S[j] == 'E':
        EW -= 1
    if S[j - 1] == 'W':
        EW += 1
    if ans > EW:
        ans = EW
print(ans)
