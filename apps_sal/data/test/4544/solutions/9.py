n = int(input())
a = list(map(int, input().split()))
num_list = [0] * 10 ** 5
for i in range(n):
    num_list[a[i]] += 1

res = 0
for i in range(1, 10 ** 5 - 1):
    res = max(res, num_list[i - 1] + num_list[i] + num_list[i + 1])

print(res)
