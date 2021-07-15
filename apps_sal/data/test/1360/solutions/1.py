tests = []
a = int(input())
for i in range(a):
    x, y = map(int, input().split(' '))
    tests.append([x, y])
s = sorted(tests, key = lambda x: (x[0], x[1]))
min1 = s[0][1]
for i in range(1, len(s)):
    if s[i][1] < min1:
        min1 = s[i][0]
    else:
        min1 = s[i][1]
print(min1)
