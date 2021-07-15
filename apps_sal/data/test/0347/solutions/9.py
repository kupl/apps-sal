m = list(map(int, input().split()))
w = list(map(int, input().split()))
n1, n2 = list(map(int, input().split()))
ans = n1 * 100 - n2 * 50
for i in range(5):
    col = 500 * (i + 1)
    ans += max(0.3 * col, (1 - m[i] / 250) * col - 50 * w[i])
print(int(ans))

