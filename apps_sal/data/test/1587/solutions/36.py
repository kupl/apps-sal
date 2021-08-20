N = int(input())
s = input()
R = 0
for i in range(N):
    if s[i] == 'R':
        R += 1
W = 0
ans = R
for i in range(N):
    if s[i] == 'R':
        R -= 1
    else:
        W += 1
    ans = min(ans, max(W, R))
print(ans)
