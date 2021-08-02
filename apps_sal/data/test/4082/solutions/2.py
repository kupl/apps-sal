n = int(input())
a = [-1] + list(map(int, input().split()))

cur = 0
l = [0] * n
m = [0] * n

for i in range(1, n + 1):
    if a[i] > a[i - 1]:
        cur += 1
    else:
        cur = 1
    l[i - 1] = cur

cur = n - 1
num = l[cur]
while cur >= 0:
    m[cur] = num
    if l[cur] == 1:
        num = l[cur - 1]
    cur -= 1

res = max(m)
a = a[1:]

for i in range(1, n - 1):
    if l[i - 1] + 2 != l[i + 1] and a[i - 1] < a[i + 1]:
        res = max(res, m[i - 1] + m[i + 1] - 1)

print(res)

# print(l)
# print(m)
