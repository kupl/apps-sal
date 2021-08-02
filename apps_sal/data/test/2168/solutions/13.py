n = int(input())
a = []
for i in range(n):
    x = list(map(int, input().split()))
    y = [x[0], max(x[1:])]
    a.append(y)
a.sort(key=lambda x: x[1])

maxx = a[-1][-1]
a.pop()

count = 0

for i in a:
    count += i[0] * (maxx - i[1])

print(count)
