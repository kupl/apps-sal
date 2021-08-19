n = int(input())
a = [int(i) for i in input().split()]
ans = sum(a)
for i in range(len(a) - 1, -1, -1):
    ans = min(ans, len(a) - i - sum(a[i:]) + sum(a[:i]))
print(len(a) - ans)
