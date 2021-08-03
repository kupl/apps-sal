n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

res = -1
cc = 0
count = 0
for i in range(2 * n):
    cc = a[cc] - 1
    count += 1
    if cc == 1:
        res = count
        break

print(res)
