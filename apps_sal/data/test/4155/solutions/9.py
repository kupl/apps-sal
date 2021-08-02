n = int(input())
H = [0] + list(map(int, input().split()))
ans = 0
for i in range(n):
    ans += max(0, H[i + 1] - H[i])
print(ans)
