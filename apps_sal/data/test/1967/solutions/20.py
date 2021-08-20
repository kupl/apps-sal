(w, h) = map(int, input().split())
a = []
res = [[0] * h for i in range(w)]
for i in range(h):
    s = input()
    for i2 in range(w):
        res[i2][h - i - 1] = s[i2]
for i in range(w):
    res[i] = res[i][::-1]
for elem in res:
    for i in range(2):
        for i2 in range(h):
            print(elem[i2], end='')
            print(elem[i2], end='')
        print()
