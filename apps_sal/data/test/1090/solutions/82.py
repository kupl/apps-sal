(N, K) = map(int, input().split())
lsS = list(input())
ans = N
if lsS[0] == 'R':
    ans -= 1
if lsS[-1] == 'L':
    ans -= 1
for i in range(N - 1):
    if lsS[i] == 'L' and lsS[i + 1] == 'R':
        ans -= 2
ans += 2 * K
ans = min(ans, N - 1)
print(ans)
