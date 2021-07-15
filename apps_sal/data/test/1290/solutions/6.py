n, m = map(int, input().split())
num = [0] * n
smth = list(map(int, input().split()))
for i in range(m):
    num[smth[i] - 1] += 1
print(min(num))
