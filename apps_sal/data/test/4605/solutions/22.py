n, a, b = map(int, input().split())
ans = 0
for i in range(1, n + 1):
    l = list(map(int, str(i)))
    sum_l = sum(l)
    if sum_l >= a and sum_l <= b:
        ans += i

print(ans)
