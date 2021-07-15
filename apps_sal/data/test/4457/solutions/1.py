n = int(input())
l = list(map(int, input().split()))
for i in range(n):
    l[i] = [l[i], i]
res = 0
l.sort()
l = l[::-1]
for i2 in range(n):
    res += i2 * l[i2][0] + 1
print(res)
for i3 in range(n):
    print(l[i3][1] + 1, end=' ')
