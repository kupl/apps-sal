
n = int(input())
a = list(map(int, input().split()))

a = [0] + a + [0]

diff = []
for i in range(1, len(a)):
    diff.append(abs(a[i - 1] - a[i]))

ans = sum(diff)

for i in range(1, len(diff)):
    tmp = abs(a[i + 1] - a[i - 1]) - abs(a[i] - a[i + 1]) - abs(a[i - 1] - a[i])
    print((ans + tmp))
