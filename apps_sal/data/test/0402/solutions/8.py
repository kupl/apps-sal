(n, k) = list(map(int, input().split()))
ans = 0
curr = 0
while curr + 5 * (ans + 1) + k <= 240:
    ans += 1
    curr += 5 * ans
print(min(n, ans))
