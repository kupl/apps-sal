n = int(input())
data = list(map(int, input().split()))
ans = 1
ans_sum = (data[0] + n - 1) // n * n
for i in range(1, n):
    k = i + (data[i] - i + n - 1) // n * n
    if k < ans_sum:
        ans = i + 1
        ans_sum = k
print(ans)
