N = int(input())
K = int(input())
lst = input().split()

ans = 0

for i in range(N):
    x = int(lst[i])
    if abs(x) < abs(K - x):
        ans += 2 * abs(x)
    else:
        ans += 2 * abs(K - x)

print(ans)
