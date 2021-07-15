x1, x2, x3, x4 = map(int, input().split())
s = [x1, x2, x3, x4]
s.sort()
for i in range(3):
    print(s[-1] - s[i], end=' ')
