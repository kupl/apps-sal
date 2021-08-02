n = int(input())
a = list(map(int, input().split()))
a = [0] + a + [0]

d_1 = []
for i in range(1, n + 2):
    d_1.append(abs(a[i] - a[i - 1]))
d_2 = []
for i in range(1, n + 1):
    d_2.append(abs(a[i + 1] - a[i - 1]))

s_d = sum(d_1)
for i in range(1, n + 1):
    print((s_d - d_1[i - 1] - d_1[i] + d_2[i - 1]))
