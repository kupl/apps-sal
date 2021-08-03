a, b, c, d, e, f = map(int, input().split())
a = 100 * a
b = 100 * b
dp1 = [0] * (f + 1)
dp2 = [0] * (f + 1)
for i in range(f + 1):
    if i % a == 0:
        if i + a <= f:
            dp1[i + a] = 1
for i in range(f + 1):
    if i == 0 or dp1[i] == 1:
        if i + b <= f:
            dp1[i + b] = 1
for i in range(f + 1):
    if i % c == 0:
        if i + c <= f:
            dp2[i + c] = 1
for i in range(f + 1):
    if i == 0 or dp2[i] == 1:
        if i + d <= f:
            dp2[i + d] = 1

ans = [-1, -1, -1]
for i in range(f + 1):
    if dp1[i] == 1:
        x = min(f - i, (i // 100) * e)
        k = -1
        for j in range(x, -1, -1):
            if dp2[j] == 1 or j == 0:
                k = j
                if ans[0] < 100 * k / (i + k):
                    ans = [100 * k / (i + k), i + k, k]
                break
print(str(ans[1]) + " " + str(ans[2]))
