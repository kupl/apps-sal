N = int(input())
S = input()
l = 0
r = S[1:N].count('E')
ans = l + r

for n in range(1, N):
    if S[n - 1] == "W":
        l += 1
    if S[n] == "E":
        r -= 1
    ans = min(ans, l + r)

print(ans)
