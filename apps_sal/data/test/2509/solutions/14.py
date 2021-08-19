N, K = map(int, input().split())

# a = pb + r
# N = 10, b = 4
# a (0...10)
# r 0,1,2,3,0,1,2,3,0,1,2
ans = 0

for b in range(1, N + 1):
    if b <= K:
        continue
    ans += ((N + 1) // b) * (b - K)
    ans += max((N + 1) % b - K, 0)
    if K == 0:
        ans -= 1
print(ans)
