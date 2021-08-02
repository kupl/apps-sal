n = int(input())
a = list(map(int, input().split()))
MAX = 100001
d = [0] * MAX
c = [0] * MAX
for i in a:
    c[i] += 1
d[1] = c[1]
for i in range(2, MAX):
    d[i] = max(d[i - 2] + i * c[i], d[i - 1])
print(d[-1])
