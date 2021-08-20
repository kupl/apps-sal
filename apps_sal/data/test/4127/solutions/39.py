(a, b) = map(str, input().split())
(i, f) = (b.split('.')[0], b.split('.')[1][0:2])
b = int(i) * 100 + int(f)
print(int(a) * b // 100)
