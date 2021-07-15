n, k, d = list(map(int, input().split()))
a = sorted(list(map(int, input().split())))
b = [0] * n
i = j = 0
for i in range(n):
    while a[i] - a[j] > d:
        j += 1
    b[i] = j
c = [0] * n
# d = [0] * n
for i in range(k - 1, n):
    # print(f'i={i}, b[i]={b[i]}, i-b[i]+1={i - b[i] + 1}, i-k={i-k}, c[i-k]={c[i-k]}, c[b[i]]={c[b[i]]}')
    # print(i - k, b[i] - 2)
    if i - b[i] + 1 >= k and (b[i] == 0 or c[i - k] > c[b[i] - 2] or (b[i] == 1 and c[i-k]> c[0])):
        c[i] = c[i - 1] + 1
        # d[i] = 1
    else:
        c[i] = c[i - 1]
# print(a)
# print(b)
# print(d)
# print(c)
print('YES' if n < 2 or c[n - 1] > c[n - 2] else 'NO')
