(n, m) = list(map(int, input().split()))
num = [int(x) for x in input().split()]
for i in range(n - 1):
    num[i + 1] += num[i]
num.insert(0, 0)
print(min(((num[i + m] - num[i], i) for i in range(n - m + 1)))[1] + 1)
