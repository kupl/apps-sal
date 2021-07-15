a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]
ans = c[0] * 100 - c[1] * 50
for i in range(5):
    ans += max(0.3 * (i + 1) * 500, (1 - a[i] / 250) * (i + 1) * 500 - 50 * b[i])
print(round(ans))
