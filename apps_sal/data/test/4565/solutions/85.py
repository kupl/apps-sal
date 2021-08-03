N = int(input())
S = list(str(input()))
east = S[1:].count('E')
ans_min = east
ans = east
for l in range(1, N):
    if S[l - 1] == 'W':
        ans += 1
    if S[l] == 'E':
        ans -= 1
    if ans <= 0:
        ans_min = 0
        break
    if ans < ans_min:
        ans_min = ans
print(ans_min)
