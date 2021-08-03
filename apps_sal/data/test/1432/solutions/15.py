n = int(input())
a = list(map(int, input().split()))
a_0 = sum(a) - 2 * sum(a[1::2])
ans = []
ans.append(a_0)
for i, A in enumerate(a[:-1], 1):
    ans.append(2 * A - ans[i - 1])

print(*ans)
