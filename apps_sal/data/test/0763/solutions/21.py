n = int(input())

a = list(map(int, input().split()))

ans = 0
e = 10 ** 9

for i in range(n):
    ne = 0
    for j in range(n):
        ne += (abs(i - j) + j + i) * 2 * a[j]

    if ne < e:
        e = ne
        ans = i

print(e)
