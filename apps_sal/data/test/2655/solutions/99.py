N = int(input())
a = list(map(int, input().split()))
a = sorted(a, reverse=True)
ans = 0
index_val = int(N // 2)
ans += a[0]
for i in range(1, index_val):
    ans += 2 * a[i]
if N % 2 != 0:
    index_val = N // 2
    ans += a[index_val]
print(ans)
