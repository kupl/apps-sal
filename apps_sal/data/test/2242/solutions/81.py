s = [int(x) for x in reversed(list(input()))]
n = len(s)
x = [0] * 2019
dp = 0
dim = 1
for si in s:
    dp = (dp + si * dim) % 2019
    x[dp] += 1
    dim = dim * 10 % 2019
ans = x[0]
for i in range(2019):
    ans += x[i] * (x[i] - 1) // 2
print(ans)
