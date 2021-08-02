import sys
n, m = map(int, input().split())
x = list(map(int, input().split()))

if n >= m or m == 1:
    print('0')
    return

x.sort()
c = []

for i in range(1, m):
    c.append(abs(x[i] - x[i - 1]))

c.sort()
print(sum(c[:len(c) - n + 1]))
