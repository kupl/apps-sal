n = int(input())
a = [[int(i) for i in input().split()], [int(i) for i in input().split()]]
s = 0
sumlist = []
for i in reversed(list(range(n))):
    s += a[0][i] + a[1][i]
    sumlist.append(s)
sumlist = [0] + sumlist

s = 0
value = [[0] * (n + 1), [0] * (n + 1)]
for i in range(n):
    s += a[0][n - i - 1] * (2 * n - i * 2 - 2) + a[1][n - i - 1] * (2 * n - 1)
    s -= sumlist[i]
    value[1][n - i - 1] = s

s = 0
for i in range(n):
    s += a[1][n - i - 1] * (2 * n - i * 2 - 2) + a[0][n - i - 1] * (2 * n - 1)
    s -= sumlist[i]
    value[0][n - i - 1] = s

ans = value[1][0]
count = 0
s = 0
#print(value)
for i in range(n):
    if i % 2 == 0:
        s += a[0][i] * (2 * i) + a[1][i] * (2 * i + 1)
    else:
        s += a[1][i] * (2 * i) + a[0][i] * (2 * i + 1)
    ans = max(ans, s + value[i % 2][(i + 1)])
  #  print(s + value[i % 2][(i + 1)])

print(ans)

