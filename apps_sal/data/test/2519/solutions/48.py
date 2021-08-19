(n, k) = map(int, input().split())
data = list(map(float, input().split()))
new_data = [0] * n
for i in range(n):
    new_data[i] = (data[i] + 1) / 2
temp = 0
for i in range(k):
    temp += new_data[i]
ans = temp
for i in range(n - k):
    temp = temp - new_data[i] + new_data[i + k]
    ans = max(ans, temp)
print(ans)
