a = list(map(int, input().split()))
sort_a = sorted(a)
ans = 0
for i in range(len(sort_a) - 1):
    ans += abs(sort_a[i] - sort_a[i + 1])
print(ans)
