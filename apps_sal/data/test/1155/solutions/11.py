n, m = [int(i) for i in input().split()]
ans = 10 ** 9
for i in range(n):
    a1, a2 = [int(i) for i in input().split()]
    ans = min(ans, a1 * m / a2)
print(ans)
