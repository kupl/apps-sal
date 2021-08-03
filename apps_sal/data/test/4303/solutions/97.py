n, k = list(map(int, input().split()))
pos = list(map(int, input().split()))
ans = 10**13
for i in range(n - k + 1):
    a1 = abs(pos[i]) + abs(pos[i] - pos[i + k - 1])
    a2 = abs(pos[i + k - 1]) + abs(pos[i] - pos[i + k - 1])
    ans = min(ans, a1, a2)
print(ans)
