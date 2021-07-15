n = int(input())
p = [int(s) for s in input().split()]

ans = 1
min_val = p[0]
for i in range(1, n):
    if p[i] <= min_val:
        min_val = p[i]
        ans += 1
print(ans)
