(r, c) = list(map(int, input().split()))
x = -1
(mini, maxi) = (10000000000.0, -10000000000.0)
for y in range(r):
    line = input()
    if 'B' in line:
        mini = min(mini, y)
        maxi = max(maxi, y)
        x = (line.find('B') + line.rfind('B')) // 2
y = (mini + maxi) // 2
print(y + 1, x + 1)
