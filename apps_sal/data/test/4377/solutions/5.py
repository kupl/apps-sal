x1, x2, x3, x4 = map(int, input().split())

s1 = max(x1, x2, x3, x4)

for i in [x1, x2, x3, x4]:
    if i != s1:
        print(s1 - i, end=' ')
