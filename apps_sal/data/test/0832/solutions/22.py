n = int(input())
a, b = [0]*n, [0]*n
for i in range(n):
    a[i], b[i] = map(int, input().split())
ans = 0
for ai in a:
    ans += b.count(ai)
print(ans)
