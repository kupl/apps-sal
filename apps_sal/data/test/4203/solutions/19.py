S = input()
N = len(S)
ans = 'AC'
if S[0] != 'A':
    ans = 'WA'
c = 0
for i in range(1, N):
    if 2 <= i <= N - 2 and S[i] == 'C':
        c += 1
    elif S[i] < 'a' or 'z' < S[i]:
        ans = 'WA'
if c != 1:
    ans = 'WA'
print(ans)
