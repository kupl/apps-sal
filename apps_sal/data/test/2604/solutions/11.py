r, d = list(map(int, input().split()))
n = int(input())
ans = 0
for _ in range(n):
    xi, yi, ri = list(map(int, input().split()))
    if (r - d + ri)**2 <= xi**2 + yi**2 and xi**2 + yi**2 <= (r - ri)**2:
        ans += 1
print(ans)
