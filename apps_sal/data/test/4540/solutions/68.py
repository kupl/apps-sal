n = int(input())
a = [0] + list(map(int, input().split())) + [0]
b = []
for i in range(n + 1):
    b.append(abs(a[i + 1] - a[i]))
temp = sum(b)

for j in range(n):
    ans = temp - b[j] - b[j + 1] + abs(a[j + 2] - a[j])
    print(ans)
