import sys
readline = sys.stdin.readline

N, X, Y = map(int, readline().split())
X -= 1
Y -= 1
ans = [0] * N
for i in range(N - 1):
    for j in range(i + 1, N):
        val = min(abs(i - j), abs(i - X) + 1 + abs(j - Y), abs(i - Y) + 1 + abs(j - X))
        ans[val] += 1

for i in range(1, len(ans)):
    print(ans[i])
