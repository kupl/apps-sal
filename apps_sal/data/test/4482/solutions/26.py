N = int(input())
a = list(map(int, input().split()))
mi = min(a)
ma = max(a)

ans = float('inf')
for i in range(mi, ma + 1):
    ans = min(ans, sum((i - ai) ** 2 for ai in a))

print(ans)
