n, m, q = list(map(int, input().split()))
a = input()
b = input()
c = [0]
for i in range(1, n + 1):
    # print(a[max(i - m, 0):i])
    c.append(c[i - 1] + (a[max(i - m, 0):i] == b))

# print(c)
for i in range(q):
    l, r = list(map(int, input().split()))
    if r - l >= m - 1:
        print(max(c[r] - c[l + m - 2], 0))
    else:
        print(0)

