n = int(input())
A = list(map(int, input().split()))
ans = 1
curr = 1
for i in range(n - 1):
    if 2 * A[i] >= A[i + 1]:
        curr += 1
    else:
        ans = max(curr, ans)
        curr = 1
ans = max(ans, curr)
print(ans)
