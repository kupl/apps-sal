ans = 0
N = int(input())
for i in range(N):
    (a, b) = map(int, input().split())
    ans += b - a + 1
print(ans)
