n = int(input())
m = [int(x) for x in input().split()]
m.sort()
sum_m = sum(m)
mean = sum_m // n
dif = sum_m - mean * n
res = 0
for i in range(n):
    if i < n - dif:
        res += abs(m[i] - mean)
    else:
        res += abs(m[i] - mean - 1)
print(res // 2)

