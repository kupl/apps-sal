n = int(input())
a = [int(i) for i in input().split()]
a = [1] + a + [10 ** 6]
mx = 10 ** 6
for i in range(len(a) - 1):
    mx = min(mx, max(a[i] - a[0], a[-1] - a[i + 1]))
print(mx)
