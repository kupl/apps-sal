import sys
n, m, x, y = list(map(int, input().split()))
x1 = max(list(map(int, input().split())))
y1 = min(list(map(int, input().split())))


for i in range(x + 1, y + 1):
    if x1 < i <= y1:
        print('No War')
        return
print('War')
