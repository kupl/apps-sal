n = int(input())
a = list(map(int, input().split()))
hako = [0] * n
for i in range(n, 0, -1):
    tmp = i
    su = 0
    while tmp <= n:
        su += hako[tmp - 1]
        tmp += i
    if su % 2 == a[i - 1]:
        continue
    else:
        hako[i - 1] = 1
print(hako.count(1))
for i in range(n):
    if hako[i] == 1:
        print(i + 1, end=' ')
