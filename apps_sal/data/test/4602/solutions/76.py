N = int(input())
K = int(input())
x = [int(i) for i in input().split()]
ans = 0
for i in range(N):
    xi = x[i]
    if xi <= K // 2:
        ans += 2 * xi
    else:
        ans += 2 * (K - xi)
print(ans)
