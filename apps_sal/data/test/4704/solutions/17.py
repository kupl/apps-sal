N = int(input())
a = list(map(int, input().split()))
s = sum(a)
data = [a[0]]
m = abs(s - 2 * a[0])
for i in range(1, N - 1):
    data.append(a[i] + data[i - 1])
for i in range(0, N - 1):
    if abs(s - 2 * data[i]) < m:
        m = abs(s - 2 * data[i])
print(m)
