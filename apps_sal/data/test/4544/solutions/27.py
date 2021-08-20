N = int(input())
a = list(map(int, input().split()))
count = [0] * (10 ** 5 + 1)
for i in range(N):
    count[a[i]] += 1
    if a[i] - 1 >= 0:
        count[a[i] - 1] += 1
    if a[i] + 1 <= 10 ** 5:
        count[a[i] + 1] += 1
max_value = max(count)
print(max_value)
